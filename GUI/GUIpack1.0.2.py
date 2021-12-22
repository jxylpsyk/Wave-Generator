import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import numpy as np
import math
import simpleaudio

#NEW GRAPHIC PACKAGE

root = tk.Tk()
root.title("Wave Generator 4.0.0.734")
root.geometry("1600x1200")
canvas = tk.Canvas(
    root, height=1200, width=1600, background="#ff8cad"
)  #,insertborderwidth=10, highlightthickness=27,highlightcolor="#fda10f",highlightbackground="#fcabbf")
canvas.grid(columnspan=300, rowspan=400)
def resize():
    cnt = 0 
    if cnt%2 == 0:
        root.geometry("1200x900")
        canvas = tk.Canvas(
             root, height=900, width=1200, background="#ff8cad"
         )  #,insertborderwidth=10, highlightthickness=27,highlightcolor="#fda10f",highlightbackground="#fcabbf")
        canvas.grid(columnspan=300, rowspan=400)
        cnt =cnt + 1
def resize1():
    cnt = 0 
    if cnt%2 == 0:
        root.geometry("1600x1200")
        canvas = tk.Canvas(
             root, height=1200, width=1600, background="#ff8cad"
         )  #,insertborderwidth=10, highlightthickness=27,highlightcolor="#fda10f",highlightbackground="#fcabbf")
        canvas.grid(columnspan=300, rowspan=400)
        cnt =cnt + 1

        
btn1= tk.Button(root,text='Make small',command=resize)
btn1.grid(row=0,column=1)
btn2= tk.Button(root,text='Make Big',command=resize1)
btn2.grid(row=0,column=0)



root.mainloop()