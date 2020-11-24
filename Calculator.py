from tkinter import *
import math

def num_c(n):
    try:
        return int(n)
    except ValueError:
        return float(n)
    
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    if number == 'x':
        e.delete(0,END)

def mathsgn(sign):
    try:
        num1 = e.get()
        e.delete(0, END)
        global f_num1
        f_num1 = num_c(num1)
        global math_sign
        math_sign = sign
        e.delete(0,END)
    except ValueError: pass

def neg_num():
    num = e.get()
    e.delete(0, END)
    num = num_c(num) * -1
    e.insert(0, num)

def equation():
    num = e.get()
    e.delete(0,END)
    try:
        if math_sign == "+": e.insert(0, f_num1+num_c(num))
        elif math_sign == "-": e.insert(0, f_num1-num_c(num))
        elif math_sign == "*": e.insert(0, f_num1*num_c(num))
        elif math_sign == "/": e.insert(0, f_num1/num_c(num))
    except ZeroDivisionError:
        e.insert(0, "divide by 0 error")
    except ValueError: pass

def percent():
    percent_val = e.get()
    e.delete(0, END), e.insert(0, str(num_c(percent_val)/100))

def dec_click():
    num = e.get()+"."
    e.delete(0, END), e.insert(0, num)
def trig(typ):
    num = e.get()
    e.delete(0, END)
    if (typ == "sin"):
        e.insert(0, math.sin(num_c(num)))
    elif (typ == "cos"):
        e.insert(0, math.cos(num_c(num)))
    elif (typ == "tan"):
        e.insert(0, math.tan(num_c(num)))
def sel(typ):
    return typ
def mode():
    def sel(typ):
        return typ

    s = Tk()
    var = IntVar()
    R1 = Radiobutton(s, text="degrees", variable=var, value=1, command=lambda:sel("deg"))
    R1.place(x = 5, y = 30)
    R2 = Radiobutton(s, text="radians", variable=var, value=2, command=lambda:sel("rad"))
    R2.place(x = 5, y = 50)

    Label(s, text = "trig").place(x = 10, y = 10)
    Label(s, text = "mode").place(x = 10, y = 10)
    var2 = IntVar()
    basic = Radiobutton(s, text="basic", variable=var2, value=1, command=lambda:sel("basic"))
    basic.place(x = 50, y = 30)
    sci = Radiobutton(s, text="scientific", variable=var2, value=2, command=lambda:sel("sci"))
    sci.place(x = 50, y = 50)
    s.mainloop()
    

root = Tk()
x = 1
root.configure(bg = 'orange'), root.title("Calculator")
e = Entry(root, width = 20)
e.grid(row = 0, column  = 0+x, columnspan = 3)
button_1 = Button(root, text = "1", bg = "grey", padx = 20, pady = 15, command = lambda: button_click(1)).grid(row = 4, column = 0+x)
button_2 = Button(root, text = "2", bg = "blue", padx = 20, pady = 15, command = lambda: button_click(2)).grid(row = 4, column = 1+x)
button_3 = Button(root, text = "3", bg = "blue", padx = 20, pady = 15, command = lambda: button_click(3)).grid(row = 4, column = 2+x)
button_4 = Button(root, text = "4", bg = "blue", padx = 20, pady = 15, command = lambda: button_click(4)).grid(row = 3, column = 0+x)
button_5 = Button(root, text = "5", bg = "blue", padx = 20, pady = 15, command = lambda: button_click(5)).grid(row = 3, column = 1+x)
button_6 = Button(root, text = "6", bg = "blue", padx = 20, pady = 15, command = lambda: button_click(6)).grid(row = 3, column = 2+x)
button_7 = Button(root, text = "7", bg = "blue", padx = 20, pady = 15, command = lambda: button_click(7)).grid(row = 2, column = 0+x)
button_8 = Button(root, activebackground = "red", text = "8", bg = "blue", padx = 20, pady = 15, command = lambda: button_click(8)).grid(row = 2, column = 1+x)
button_9 = Button(root, text = "9", fg = "blue", padx = 20, pady = 15, command = lambda: button_click(9)).grid(row = 2, column = 2+x)
button_0 = Button(root, text = "0", padx = 52, pady = 15, command = lambda: button_click(0)).grid(row = 5, column = 0+x, columnspan = 2)
button_add = Button(root, text = "+", padx = 20, pady = 15, command = lambda: mathsgn('+')).grid(row = 4, column = 3+x)
button_subt = Button(root, text = "-", padx = 20, pady = 15, command = lambda: mathsgn('-')).grid(row = 3, column = 3+x)
button_mult = Button(root, text = "*", padx = 20, pady = 15, command = lambda: mathsgn('*')).grid(row = 2, column = 3+x)
button_divide = Button(root, text = "/", padx = 20, pady = 15, command = lambda: mathsgn('/')).grid(row = 1, column = 3+x)
button_equal = Button(root, text = "=", padx = 20, pady = 15, command = equation).grid(row = 5, column = 3+x)
button_clear = Button(root, text = "AC", padx = 15, pady = 15, command = lambda: button_click('x')).grid(row = 1, column = 0+x)
button_percent = Button(root, text = "%", padx = 20, pady = 15, command = percent).grid(row = 1, column = 2+x)              
button_neg = Button(root, text = "+/-", padx = 15, pady = 15, command = neg_num).grid(row = 1, column = 1+x)
button_decimal = Button(root, text = ".", padx = 20, pady = 15, command = dec_click).grid(row = 5, column = 2+x)
#button_sin = Button(root, text = "sin", padx = 20, pady = 15, command = lambda: trig("sin")).grid(row = 2, column = 0)
#button_cos = Button(root, text = "cos", padx = 20, pady = 15, command = lambda: trig("cos")).grid(row = 3, column = 0)
#button_tan = Button(root, text = "tan", padx = 20, pady = 15, command = lambda: trig("tan")).grid(row = 4, column = 0)


root.bind("1", lambda event: button_click(1)), root.bind("2", lambda event: button_click(2)), root.bind("3", lambda event: button_click(3)), root.bind("4", lambda event: button_click(4))
root.bind("5", lambda event: button_click(5)), root.bind("6", lambda event: button_click(6)), root.bind("7", lambda event: button_click(7)), root.bind("8", lambda event: button_click(8))
root.bind("9", lambda event: button_click(9)), root.bind("0", lambda event: button_click(0)), root.bind("+", lambda event: mathsgn("+")), root.bind("-", lambda event: mathsgn("-"))
root.bind("*", lambda event: mathsgn("*")), root.bind("x", lambda event: mathsgn("x")), root.bind("/", lambda event: mathsgn("/")), root.bind("=", lambda event: equation())
root.bind("<Return>", lambda event: equation())
root.bind(".", lambda event: dec_click()), root.bind("%", lambda event: percent()), root.bind("c", lambda event: button_click("x"))
#root.bind("s", lambda event: trig("sin"))
#root.bind("co", lambda event: trig("cos"))
#root.bind("t", lambda event: trig("tan"))

root.mainloop()
