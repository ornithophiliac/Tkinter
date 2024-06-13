from tkinter import *

mukul_root = Tk()

#widthxheight
mukul_root.geometry("644x434")

#width,height
mukul_root.minsize(200,100)

#width,height
mukul_root.maxsize(500,600)

mukul = Label(text="Mukul is a good boy")
mukul.pack()

mukul_root.mainloop()