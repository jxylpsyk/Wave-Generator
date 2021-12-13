from tkinter import *


def clicked():

    res = "Jai " + txt.get()

    lbl.configure(text=res)


window = Tk()
window.title("Fish")
window.geometry('1104x721')
window.configure(background='#77A0BB')

lbl = Label(window, text="Hello")
lbl.configure(background='#77A0BB')
lbl.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.configure(background='#77A0BB')
txt.grid(column=1, row=0)

btn = Button(window,
             text="Chesnut Kranky Alpha",
             highlightbackground='#77A0BB', # use this for mac, other stuff doesn't work on windows
             command=clicked)
btn.grid(column=2, row=0)

window.mainloop()