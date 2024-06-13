from tkinter import *

root = Tk()

root.geometry("500x500")

f1 = Frame(root,bg="grey", borderwidth=5, relief=SUNKEN)
f1.pack(side=LEFT,pady=0,fill=Y)

f2 = Frame(root,bg="grey", borderwidth=5, relief=SUNKEN)
f2.pack(side=TOP,pady=0,fill=X)

l1 = Label(f1,text="Project Tkinter - Pycharm")
l1.pack(pady=5)

l2 = Label(f2,text="Welcome to Sublime Text")
l2.pack()

root.mainloop()