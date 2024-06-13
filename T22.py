from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Scrollbar")

#for connecting the scrollbar to widget
#1. widget(yscrollcommand=scrollbar.set
#scrollbar.config((command=widget.yview
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
listbox = Listbox(root, yscrollcommand = scrollbar.set)
for i in range(344):
    listbox.insert(END,f"Item{i}")
listbox.pack(fill="both")
scrollbar.config(command=listbox.yview)
root.mainloop()