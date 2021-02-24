from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict ={}
#Data
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orignal_data = pandas.read_csv("data/french_words.csv")
    data_dict = orignal_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient= "records")

#Logic
def next_word():
    global current_card, flip_card_timer
    window.after_cancel(flip_card_timer)
    current_card = choice(data_dict)
    canvas.itemconfig(canvas_image, image = card_front_image)
    canvas.itemconfig(card_title, text="French", fill = "black")
    canvas.itemconfig(card_word, text = current_card["French"], fill = "black")
    flip_card_timer = window.after(3000, func=word_meaning)


def word_meaning():
    global current_card

    canvas.itemconfig(canvas_image, image = card_back_image)
    canvas.itemconfig(card_title, text="English", fill = "white")
    canvas.itemconfig(card_word, text = current_card["English"], fill = "white")

def is_known():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index= False)
    next_word()



#window
window = Tk()
window.title("Flashy")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)
flip_card_timer = window.after(3000, func=word_meaning)

#canvas
canvas = Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR, highlightthickness = 0)
card_front_image = PhotoImage(file = "images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image = card_front_image)
card_title = canvas.create_text(400, 150, text = "", font = ("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text = "", font = ("Ariel", 60, "bold"))
canvas.grid(row = 0, column = 0, columnspan =2)



#Button
cross_image = PhotoImage(file= "images/wrong.png")
unknown_button = Button(image = cross_image, bg = BACKGROUND_COLOR, command = next_word)
unknown_button.grid(row = 1, column = 0)

check_image = PhotoImage(file = "images/right.png")
known_button = Button(image = check_image, bg = BACKGROUND_COLOR, command = is_known)
known_button.grid(row = 1, column = 1)


next_word()


window.mainloop()

