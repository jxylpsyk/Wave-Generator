import tkinter as tk
from PIL import Image,ImageTk,ImageDraw

from default_waves import *
'''
colours pinkish red #ff8cad
mellow yellow #ffff8c
Pretty purple #c800ff
Bratty blue #2600ff
Plain Blanc #ffffff
!!!ALWAYS KEEP MIN ROW AS 1
'''
def a1():
    print ('hello world')

root = tk.Tk()
root.title("Wave Generator 4.0.0.734")
canvas = tk.Canvas(root,height=900,width=300,background= "#ff8cad")#,insertborderwidth=10, highlightthickness=27,highlightcolor="#fda10f",highlightbackground="#fcabbf")
canvas.grid(columnspan=15,rowspan=100)
box = tk.Canvas(root,height = 900, width = 1200, background = "#ffff8c")
box.grid(column= 15,row=1,columnspan=100,rowspan=100)

tsxt1 = tk.Label(text = "Wave Generator",height= 0
                 ,background="#ff8cad",)
tsxt1.grid(row=1)

txtbx1 = tk.Button(root,width=12,height=2,text="Square",background = '#2600ff',foreground="#ffffff",)
txtbx1.grid(column = 1,row = 32)

txtbx1 = tk.Button(root,width=12,height=2,text="SawTooth",background='#2600ff',foreground="#ffffff",)
txtbx1.grid(column = 9,row = 32)

txtbx1 = tk.Button(root,width=12,height=2,text="Triangle",background='#c800ff',foreground="#ffffff",)
txtbx1.grid(column = 1,row = 35)

txtbx1 = tk.Button(root,width=12,height=2,text="Sine",background= '#c800ff',foreground="#ffffff",)
txtbx1.grid(column = 9,row =35)

root.mainloop()