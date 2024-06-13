from tkinter import *

root = Tk()

root.geometry("500x500")
def hello():
    print("Hello Mukul")


frame = Frame(root,borderwidth=6,background="grey",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")

b1= Button(frame , fg="red", text="Print Now",command=hello)
b1.pack()

root.mainloop()