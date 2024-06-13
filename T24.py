from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Status Bar")
def upload():
    statusvar.set("Busy..")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready Now")

statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root, textvariable = statusvar, relief =SUNKEN, anchor="w")
sbar.pack(side=TOP,fill=X)
Button(root,text="Upload",command=upload).pack()
root.mainloop()