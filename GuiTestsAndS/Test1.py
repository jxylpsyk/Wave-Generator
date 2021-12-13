import tkinter as tk
import PyPDF2 as pp
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

canvas = tk.Canvas(root, width = 600, height = 450)
canvas.grid(columnspan=3,rowspan=3)
#logo
logo = Image.open('logo.jpeg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image=logo
logo_label.grid(column=1, row=0)
#instructions
instructions=tk.Label(root,text="Select a PDF file on your computer to extract all its text", font= "Raleway")
instructions.grid(columnspan=3,column=0,row=1)

#Browse Button
browse_text = tk.StringVar()
browsebtn = tk.Button(root,textvariable=browse_text,command=lambda:openfile(), font="Raleway",bg="#fab1d7",height=4,width=30)
browse_text.set("Browse")
browsebtn.grid(column=1,row= 2)

def openfile():
    browse_text.set("Loading...")
    file = askopenfile(parent = root, mode = 'rb', title = "Choose a File", filetype= [("Pdf file","*.pdf")])
    if file:
        readpdf = pp.PdfFileReader(file)
        page = readpdf.getPage(0)
        page_content = page.extractText()
        #textbox
        
        textbox = tk.Text(root,height=20,width=100,padx=50,pady=50)
        textbox.insert(1.0, page_content)
        textbox.tag_config("center", justify="center")
        textbox.tag_add("center",1.0,"end")
        textbox.grid(column=1,row=3)
        browse_text.set("Browse")
    else:
        browse_text.set("Browse")
 
canvas = tk.Canvas(root, width = 600, height = 150)
canvas.grid(columnspan=3)

root.mainloop()
