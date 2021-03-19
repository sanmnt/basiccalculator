from tkinter import *

root = Tk()
root.title("Basic Calculator")

e= Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def clickButton(number):
    n = e.get()
    e.delete(0, END)
    e.insert(0, str(n) + str(number))

def clearButton():
    e.delete(0, END)
def addButton():
    initialNumber = e.get()
    global iNum
    global math
    math = "addition"
    iNum = int(initialNumber)
    e.delete(0, END)
def subtractButton():
    initialNumber = e.get()
    global iNum
    global math
    math = "subtraction"
    iNum = int(initialNumber)
    e.delete(0, END)
def multiplyButton():
    initialNumber = e.get()
    global iNum
    global math
    math = "multiplication"
    iNum = int(initialNumber)
    e.delete(0, END)
def divideButton():
    initialNumber = e.get()
    global iNum
    global math
    math = "division"
    iNum = int(initialNumber)
    e.delete(0, END)
def equalButton():
    secondNumber = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, iNum + int(secondNumber))
    if math == "subtraction":
        e.insert(0, iNum - int(secondNumber))
    if math == "multiplication":
        e.insert(0, iNum * int(secondNumber))
    if math == "division":
        e.insert(0, iNum / int(secondNumber))
#Define buttons
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: clickButton(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: clickButton(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: clickButton(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: clickButton(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: clickButton(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: clickButton(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: clickButton(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: clickButton(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: clickButton(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: clickButton(0))
button_add = Button(root, text="+", padx=40, pady=20, command=addButton)
button_subtract = Button(root, text="-", padx=40, pady=20, command=subtractButton)
button_multiply = Button(root, text="*", padx=40, pady=20, command=multiplyButton)
button_divide = Button(root, text="/", padx=40, pady=20, command=divideButton)
button_equal = Button(root, text="=", padx=40, pady=20, command=equalButton)
button_clear = Button(root, text="Clear", padx=40, pady=20, command=clearButton)
#Put buttons on screen
button0.grid(row=4, column=1)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button_add.grid(row=4, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=1, column=3)

button_equal.grid(row=4, column=2)
button_clear.grid(row=4, column=0)

root.mainloop()