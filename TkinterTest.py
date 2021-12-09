from tkinter import *
import emoji

window = Tk()

window.title("Anti Terrosrist Organization truly and spiritually criminally not inclined")

window.geometry('350x200')

window.configure(background='#77A0BB')

lbl = Label(window, text="Hello")

lbl.configure(background='#77A0BB')

lbl.grid(column=0, row=0)

txt = Entry(window, width=10)

txt.configure(background='#FFA500')

txt.grid(column=1, row=0)

def islamicKhalifate():
    x = 1
    a = input("Are you my khalifa:   ")
    if a == 'Yes' or a == 'yes':
        while x < 100:
            print('Hail my great khalifa')
    else:
        while x < 100:
            print('Die african slave')


def clicked():

    res = "Jai " + txt.get()

    lbl.configure(text=res)


btn = Button(window, text="Chesnut Kranky Alpha", command=clicked)

btn.grid(column=2, row=0)
 
btn1 = Button(window, text="Rainy day", command= islamicKhalifate())
btn1.grid(column=3, row=10)
window.mainloop()