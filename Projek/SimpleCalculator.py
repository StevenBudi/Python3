from tkinter import *

root = Tk()
root.title("Calculator")
entry1 = Entry(root, width = 65, borderwidth = 5)
entry1.grid(row=0, column=0, columnspan = 5, padx =10, pady = 10)

def button_click(number):
    current = entry1.get()
    entry1.delete(0, END)
    entry1.insert(0, str(current) + str(number))

def clear():
    entry1.delete(0, END)

def add():
    global status
    status = "addition"
    first_num = entry1.get()
    global f_num 
    f_num = int(first_num)
    entry1.delete(0, END)

def substract():
    global status
    status = "substraction"
    first_num = entry1.get()
    global f_num 
    f_num = int(first_num)
    entry1.delete(0, END)

def multiply():
    global status
    status = "multiply"
    first_num = entry1.get()
    global f_num 
    f_num = int(first_num)
    entry1.delete(0, END)

def divide():
    global status
    status = "division"
    first_num = entry1.get()
    global f_num 
    f_num = int(first_num)
    entry1.delete(0, END)

def equal():
    if status == "addition":
        second_num = entry1.get()
        entry1.delete(0, END)
        entry1.insert(0, f_num + int(second_num))
    
    if status == "substraction":
        second_num = entry1.get()
        entry1.delete(0, END)
        entry1.insert(0, f_num - int(second_num))

    if status == "multiply":
        second_num = entry1.get()
        entry1.delete(0, END)
        entry1.insert(0, f_num * int(second_num))
    
    if status == "division":
        second_num = entry1.get()
        entry1.delete(0, END)
        entry1.insert(0, f_num / int(second_num))




button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))
button_0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))
button_clear = Button(root, text = "Clear", padx = 79, pady = 20, command = clear)
button_add = Button(root, text = "+", padx = 40, pady = 20, command = add)
button_diff = Button(root, text = "-", padx = 40, pady = 20, command = substract)
button_mul = Button(root, text = "x", padx = 40, pady = 20, command = multiply)
button_div = Button(root, text = "/", padx = 40, pady = 20, command= divide)
button_equal = Button(root, text = "=", padx = 86.5, pady = 20, command = equal)


button_1.grid(column = 0, row = 3 )
button_2.grid(column = 1, row = 3 )
button_3.grid(column = 2, row = 3 )

button_4.grid(column = 0, row = 2 )
button_5.grid(column = 1, row = 2 )
button_6.grid(column = 2, row = 2 )

button_7.grid(column = 0, row = 1 )
button_8.grid(column = 1, row = 1 )
button_9.grid(column = 2, row = 1 )

button_0.grid(column = 0, row = 4 )
button_clear.grid(column = 3, row = 2, columnspan = 2)
button_equal.grid(column = 1, row =  4, columnspan = 2)

button_add.grid(column = 3, row = 3)
button_diff.grid(column = 4, row = 3)
button_mul.grid(column = 3, row = 4)
button_div.grid(column = 4, row = 4)

root.mainloop()