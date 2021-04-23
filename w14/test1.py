"""
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

"""
import builtins
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Jorge Cortes. Learning from https://www.youtube.com/watch?v=YXPyB4XeYLA ')
root.iconbitmap('c:\deleteme\python.ico')

frame = LabelFrame(root, padx=150, pady=150)
frame.pack(padx=150, pady=150)

b = Button(frame,  text='List')
b2 = Button(frame, text='Add')
b3 = Button(frame, text='Remove')
b4 = Button(frame, text='Edit')
b5 = Button(frame, text='Search')


b.grid(row=0,  column=0)
b2.grid(row=1, column=0)
b3.grid(row=2, column=0)
b4.grid(row=3, column=0)
b5.grid(row=4, column=0)




root.mainloop()
