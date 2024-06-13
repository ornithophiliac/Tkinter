from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("PyCharm")
def myfunc():
    print("Hello world mukul pune jaa rhay yeahh")
# use this to create a non dropdown menu
# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit",command=quit)
#
# root.config(menu=mymenu)

yourmenubar = Menu(root)
m1 = Menu(yourmenubar,tearoff=0)
m1.add_command(label="New Project",command=myfunc)
m1.add_command(label="Save",command=myfunc)
m1.add_command(label="Save As",command=myfunc)
m1.add_command(label="Print",command=myfunc)
yourmenubar.add_cascade(label="File",menu=m1)
root.config(menu=yourmenubar)
root.mainloop()