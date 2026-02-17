import tkinter as tk
import math

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")



root = tk.Tk()
root.title("Scientific Calculator")

equation = tk.StringVar()
expression_field = tk.Entry(root, textvariable=equation)
expression_field.grid(columnspan=4)

tk.Button(root, text='C', command=clear, height=1, width=7).grid(row=2, column=0)
tk.Button(root, text='√', command=lambda: press('math.sqrt('), height=1, width=7).grid(row=2, column=1)
tk.Button(root, text='(', command=lambda: press('('), height=1, width=7).grid(row=2, column=2)
tk.Button(root, text=')', command=lambda: press(')'), height=1, width=7).grid(row=2, column=3)

tk.Button(root, text='sin', command=lambda: press('math.sin('), height=1, width=7).grid(row=3, column=0)
tk.Button(root, text='cos', command=lambda: press('math.cos('), height=1, width=7).grid(row=3, column=1)
tk.Button(root, text='tan', command=lambda: press('math.tan('), height=1, width=7).grid(row=3, column=2)
tk.Button(root, text='/', command=lambda: press('/'), height=1, width=7).grid(row=3, column=3)

tk.Button(root, text='7', command=lambda: press(7), height=1, width=7).grid(row=4, column=0)
tk.Button(root, text='8', command=lambda: press(8), height=1, width=7).grid(row=4, column=1)
tk.Button(root, text='9', command=lambda: press(9), height=1, width=7).grid(row=4, column=2)
tk.Button(root, text='*', command=lambda: press('*'), height=1, width=7).grid(row=4, column=3)

tk.Button(root, text='4', command=lambda: press(4), height=1, width=7).grid(row=5, column=0)
tk.Button(root, text='5', command=lambda: press(5), height=1, width=7).grid(row=5, column=1)
tk.Button(root, text='6', command=lambda: press(6), height=1, width=7).grid(row=5, column=2)
tk.Button(root, text='-', command=lambda: press('-'), height=1, width=7).grid(row=5, column=3)

tk.Button(root, text='1', command=lambda: press(1), height=1, width=7).grid(row=6, column=0)
tk.Button(root, text='2', command=lambda: press(2), height=1, width=7).grid(row=6, column=1)
tk.Button(root, text='3', command=lambda: press(3), height=1, width=7).grid(row=6, column=2)
tk.Button(root, text='+', command=lambda: press('+'), height=1, width=7).grid(row=6, column=3)

tk.Button(root, text='0', command=lambda: press(0), height=1, width=7).grid(row=7, column=0)
tk.Button(root, text='.', command=lambda: press('.'), height=1, width=7).grid(row=7, column=1)
tk.Button(root, text='π', command=lambda: press('math.pi'), height=1, width=7).grid(row=7, column=2)
tk.Button(root, text='=', command=equalpress, height=1, width=7).grid(row=7, column=3)

root.mainloop()