from tkinter import *
root= Tk()

root.geometry("4000x5000")
root.title("Mukul Ka First Gui")

#important label options
# text - adds text
# bd - Background
# fg - foreground
# ffont - ssets font
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text='''Python Tkinter Geometry
The Tkinter geometry specifies the method by using which, the widgets are represented on display. The python Tkinter provides the following geometry methods.

The pack() method
The grid() method
The place() method
Let's discuss each one of them in detail.

Python Tkinter pack() method
The pack() widget is used to organize widget in the block. The positions widgets added to the python application using the pack() method can be controlled by using the various options specified in the method call.

However, the controls are less and widgets are generally added in the less organized manner.

The syntax to use the pack() is given below.''', bg="red" , fg="white" , padx=0 , pady=0 ,font="comicsansms 10 bold", borderwidth=3, relief=SUNKEN)

# important pack optionss
# anchor -  nw
# side - top, bottomm, left, right
# fill -
# padx
# pady

title_label.pack(side=BOTTOM,anchor="sw",fill=Y,padx=15,pady=90)
root.mainloop()