from tkinter import *

import pandas
import pandas as pd
import random
import json

BACKGROUND_COLOR = "#B1DDC6"
words_dict = {}

# data processing
try:
    words_data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    words_dict = original_data.to_dict(orient="records")
else:
    words_dict = words_data.to_dict(orient="records")
selected_word = random.choice(words_dict)
word_keys = list(selected_word.keys())

try:
    with open("words_to_learn.csv") as learned_words:
        print(learned_words.read())
except:
    print("sad")


def generate_new_word():
    global selected_word, flip_timer
    window.after_cancel(flip_timer)
    selected_word = random.choice(words_dict)
    canvas.itemconfig(title_text, text=word_keys[0], fill="#000000")
    canvas.itemconfig(word_text, text=selected_word[word_keys[0]], fill="#000000")
    canvas.itemconfig(canvas_img, image=card_front_img)
    flip_timer = window.after(3000, func=word_translation)


def generate_new_word_know():
    global selected_word
    words_dict.remove(selected_word)

    data = pd.DataFrame(words_dict)
    data.to_csv("data/words_to_learn.csv", index=False

    generate_new_word()


def word_translation():
    global selected_word
    canvas.itemconfig(title_text, text=word_keys[1], fill="#ffffff")
    canvas.itemconfig(word_text, text=selected_word[word_keys[1]], fill="#ffffff")
    canvas.itemconfig(canvas_img, image=card_back_img)


# end data processing

# ui setup
window = Tk()
window.title("Flash Card Game")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=word_translation)

canvas = Canvas(bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=generate_new_word_know)
right_btn.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=generate_new_word)
wrong_btn.grid(column=0, row=1)
# end ui setup


generate_new_word()

window.mainloop()
