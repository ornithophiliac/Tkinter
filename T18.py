from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("500x500")
root.title("PyCharm")
def myfunc():
    print("Hello world mukul pune jaa rhay yeahh")
def help():
    print("Mai karunga teri help")
    a = tmsg.showinfo("Help","Mai karunga teri help")
def rate():
    print("Pleasse rate us")
    b = tmsg.askquestion("Wass your experience good","was expeirence good?")
    if b == "yes":
        msg = "Great Rate us on appstore"
    else:
        msg = "Oh sorry to hear that"
    tmsg.showinfo("Experience",msg)

def friend():
    ans = tmsg.askretrycancel("Mukul se dosti krlo","Sorry to hear that ")
    if ans:
        print("Retry krne par bhi kuch nahi hoga")
    else:
        print("Badhiya accha hua cancel kiya warna bahot marunga")

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

m2 = Menu(yourmenubar,tearoff=0)
m2.add_command(label="New Project",command=myfunc)
m2.add_command(label="Save",command=myfunc)
m2.add_command(label="Save As",command=myfunc)
m2.add_command(label="Print",command=myfunc)
yourmenubar.add_cascade(label="Edit",menu=m2)
root.config(menu=yourmenubar)

m3 = Menu(yourmenubar,tearoff=0)
m3.add_command(label="Sachmei Help",command=help)
m3.add_command(label="Rate",command=rate)
m3.add_command(label="Befriend Dev",command=friend)
yourmenubar.add_cascade(label="HELP",menu=m3)
root.config(menu=yourmenubar)

root.mainloop()