from tkinter import *

root = Tk()
root.title("Prime Number Checker")

def checker():
    text1.delete("1.0", END)
    entry = entry1.get()
    entry = int(entry)
    factors = []
    status = " "
    for i in range(1, entry + 1):
        if entry % i == 0:
            factors.append(i)
    if len(factors) <= 2:
        status = " is a prime number"
        text1.insert(END, (str(entry)+ status))
    else :
        status = " isn't a prime number"
        text1.insert(END, (str(entry)+ status))

    



entry1 = Entry(root)
entry1.pack()
entry1.insert(0, "Enter Your Number")
button1 = Button(root, text= "Check", command= checker )
button1.pack()
text1 = Text(root, height= 1, width = 30)
text1.pack()


root.mainloop()