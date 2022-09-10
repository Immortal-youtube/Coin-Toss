


from tkinter import *
import os
import random

def coin_toss():
    text = random.randint(0,1)
    if text == 1:
        option.config(text="Heads")
    else:
        option.config(text="Tails")

window = Tk()
window.geometry("500x500")
icon = PhotoImage(file=os.path.dirname(__file__) + "/coin.png")
window.iconphoto(False,icon)
window.title("Coin Toss")
window.configure(background="black")
option = Label(window,text="Roll to see your option",font=("Ariel",30),foreground="white",background="Black")
roll = Button(window,text="Roll",font=("Ariel",30),foreground="Blue",background="black",height=200,width=500,command=lambda: coin_toss())
option.pack(anchor='center')
roll.pack(side="bottom")
window.mainloop()