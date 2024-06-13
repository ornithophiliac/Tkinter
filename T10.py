from tkinter import *

root=Tk()

root.geometry("500x500")
def getvalues():
    print(uservalue.get())
    print(passwordvalue.get())

user = Label(root,text="Username")
password = Label(root,text="Password")
user.grid()
password.grid()

# Variable classses in tkinter
# boolean var doublevar intvar stringvar

uservalue = StringVar()
passwordvalue = StringVar()

userentry = Entry(root,textvariable=uservalue)
passwordentry = Entry(root,textvariable=passwordvalue)

Button(text="Submit", command=getvalues).grid()

userentry.grid(row=0,column=1)
passwordentry.grid(row=1,column=1)



root.mainloop()