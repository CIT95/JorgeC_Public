
import builtins
from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title('Student DB') 
frame = Frame(root, padx=150, pady=10)
frame.pack(padx=150, pady=50)

#frame = LabelFrame(root, padx=150, pady=150)
#frame.pack(padx=150, pady=150)

topframe = LabelFrame(root,padx=150, pady=10)
topframe.pack( side = TOP)

bt1 = Button(topframe, text="List", padx=30, pady=10)
bt1.pack(side = LEFT)
bt2 = Button(topframe, text="Add", padx=30, pady=10)
bt2.pack(side = LEFT)
bt3 = Button(topframe, text="Remove", padx=30, pady=10) 
bt3.pack(side = LEFT)
bt4 = Button(topframe, text="Edit", padx=30, pady=10)
bt4.pack(side = LEFT)
bt4 = Button(topframe, text="Search", padx=30, pady=10)
bt4.pack(side = LEFT)

root.mainloop()

