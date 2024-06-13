from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("500x500")
root.title("Aaj tera bhai slider banayega")
def getdollars():
    print( f"We have credited {myslider2.get()} dollars to your bank account")
    tmsg.showinfo("Amount Credited",f"We have credited {myslider2.get()} dollars to your bank account")
# myslider = Scale(root, from_=0 , to=100)
# myslider.pack()
Label(root,text="How many dollars do you want?").pack()
myslider2 = Scale(root, from_=0 , to=100 , orient=HORIZONTAL,tickinterval=50)
myslider2.set(5)

Button(root,text="Get dollars!!",command=getdollars).pack()
myslider2.pack()
root.mainloop()