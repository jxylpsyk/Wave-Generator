import tkinter as tk

def a1():
    print ('hello world')

root = tk.Tk()
canvas = tk.Canvas(root,height=900,width=1200,background= "#faaffa",insertborderwidth=10, highlightthickness=27,highlightcolor="#fda10f",highlightbackground="#fcabbf")
canvas.grid(columnspan=15,rowspan=15)
txtbx1 = tk.Button(root,width=10,height=4)
txtbx1.grid(column = 3,row = 3)
root.mainloop()