from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card Game")
window.config(bg=BACKGROUND_COLOR, width=1000, height=700)

canvas = Canvas(bg=BACKGROUND_COLOR)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(500, 300, image=card_front_img)
canvas.create_text(500, 200, text="Title", font=("Arial", 24, "italic"))
canvas.create_text(500, 300, text="Word", font=("Arial", 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2, rowspan=3)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0)
right_btn.grid(column=1, row=3)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0)

window.mainloop()
