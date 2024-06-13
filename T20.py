from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("500x500")
root.title("Aaj radiobutton banayenge")
def order():
    tmsg.showinfo("Order received",f"We have received your order for {var.get()}. Thanks for ordering")

var = IntVar()
# var.set(1)
Label(root,text="Kya khaoge bey?", justify=LEFT,padx=14).pack()
radio = Radiobutton(root,text="Dosa",padx=14,variable=var,value=1).pack(anchor="w")
radio = Radiobutton(root,text="Idli",padx=14,variable=var,value=2).pack(anchor="w")
radio = Radiobutton(root,text="Paratha",padx=14,variable=var,value=3).pack(anchor="w")
radio = Radiobutton(root,text="Samosa",padx=14,variable=var,value=4).pack(anchor="w")

Button(text="Order now",command=order).pack()
root.mainloop()