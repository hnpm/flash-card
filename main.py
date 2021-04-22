from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="images/card_front.png")
cross_image = PhotoImage(file="images/wrong.png")
check_image = PhotoImage(file="images/right.png")

canvas = Canvas(width=800, height=526)
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)

known_button = Button(image=check_image, highlightthickness=0)
known_button.grid(row=1, column=1)


window.mainloop()
