"""
https://www.youtube.com/watch?v=YXPyB4XeYLA
Using tkinter GUI environment for python
Apr/13/21
* Improving when the user divides by 0
* Improving once you hit = (equal) and click in any number for a next operation it will first clear the screen

"""
bflag1 = False
from tkinter import *
from tkinter import messagebox
from typing import Match


root = Tk()
root.title('Simple Calculator. JC')

e = Entry(root, width=35, borderwidth=5, font=5)
e.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

def button_click(number):
    global bflag1   
    if bflag1:
       e.delete(0, END)
       bflag1 = False    
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    e.delete(0, END)
    

def button_equal():    
    second_number = e.get()
    global bflag1
    e.delete(0, END)
    if math == 'addition':
       e.insert(0, f_num + int(second_number))
       bflag1 = True
    if math == 'substraction':
       e.insert(0, f_num - int(second_number))
       bflag1 = True
    if math == 'multiplication':
       e.insert(0, f_num * int(second_number))
       bflag1 = True
    if math == 'division':
        if int(second_number) == 0:                       
            e.insert(0, 'Error, division by Zero')
        else:
            e.insert(0, f_num / int(second_number))
        bflag1 = True    

def button_substract():
    first_number = e.get()
    global f_num     
    global math
    math = 'substraction'
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num     
    global math
    math = 'multiplication'
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num     
    global math
    math = 'division'
    f_num = int(first_number)
    e.delete(0, END)


#  define buttons
button_1 = Button(root, text='1',  padx=40, pady=25, command=lambda: button_click(1))
button_2 = Button(root, text='2',  padx=40, pady=25, command=lambda: button_click(2))
button_3 = Button(root, text='3',  padx=40, pady=25, command=lambda: button_click(3))
button_4 = Button(root, text='4',  padx=40, pady=25, command=lambda: button_click(4))
button_5 = Button(root, text='5',  padx=40, pady=25, command=lambda: button_click(5))
button_6 = Button(root, text='6',  padx=40, pady=25, command=lambda: button_click(6))
button_7 = Button(root, text='7',  padx=40, pady=25, command=lambda: button_click(7))
button_8 = Button(root, text='8',  padx=40, pady=25, command=lambda: button_click(8))
button_9 = Button(root, text='9',  padx=40, pady=25, command=lambda: button_click(9))
button_0 = Button(root, text='0',  padx=40, pady=25, command=lambda: button_click(0))
button_add = Button(root, text='+',  padx=39, pady=25, command=button_add)
button_equal = Button(root, text='=',     padx=91, pady=25, command=button_equal)
button_clear =  Button(root, text='Clear', padx=79, pady=25, command=button_clear)

button_substract = Button(root, text='-', padx=41, pady=25, command=button_substract)
button_multiply = Button(root, text='*', padx=40, pady=25, command=button_multiply)
button_divide =  Button(root, text='/', padx=41, pady=25, command=button_divide)

#  put the buttons on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4, column=1,columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1,columnspan=2)

button_substract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)


root.mainloop()