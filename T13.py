from tkinter import *
root = Tk()

canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root , width=canvas_width , height=canvas_height)
can_widget.pack()

can_widget.create_line(0,100,200,300) #create a line from x1,y1 to x2,y2
can_widget.create_rectangle(3,5,700,400) #create a rectangle by taking upper left corner to bottom right corner
can_widget.create_text(200,200,text="hello")
can_widget.create_oval(344,255,126,321)
root.mainloop()