from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# Change Word
def change_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


# Flip Card
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    to_learn.remove(current_card)
    file = pd.DataFrame(to_learn)
    file.to_csv("data/words_to_learn.csv", index=False)
    change_word()


window = Tk()
window.title('Flashy Card')
window.config(padx=100, pady=100, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=562, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "bold"))
card_word = canvas.create_text(400, 350, text="", font=("Arial", 40, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

# Wrong Button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_btn = Button(command=change_word, image=wrong_image, highlightthickness=0)
wrong_btn.grid(row=1, column=0)

# Right Button
right_image = PhotoImage(file="images/right.png")
right_btn = Button(command=is_known, image=right_image, highlightthickness=0)
right_btn.grid(row=1, column=1)

change_word()

window.mainloop()

