from tkinter import *
from PIL import Image, ImageTk
mukul_root = Tk()

mukul_root.geometry("833x244")

#photo = PhotoImage(file="ai 1 gl.png")

#for jpg images

image = Image.open('ai 2 gl.jpg')
photo = ImageTk.PhotoImage(image)
mukul_label = Label(image=photo)
mukul_label.pack()

mukul_root.mainloop()
