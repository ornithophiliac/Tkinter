from tkinter import *
def Mukul(event):
    print("you ccliccked me")
root = Tk()
root.title("Mukul Karaye Events")
root.geometry("500x500")
widget = Button(root,text="Fcuk me please")
widget.pack()
widget.bind('<Button-1>', Mukul)
root.mainloop()