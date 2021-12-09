from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

window.configure(background='#77A0BB')

lbl = Label(window, text="Hello")

lbl.configure(background='#77A0BB')

lbl.grid(column=0, row=0)

txt = Entry(window, width=10)

txt.configure(background='#77A0BB')

txt.grid(column=1, row=0)


def clicked():

    res = "Welcome to " + txt.get()

    lbl.configure(text=res)


btn = Button(window, text="Hell No", command=clicked)

btn.grid(column=2, row=0)

window.mainloop()