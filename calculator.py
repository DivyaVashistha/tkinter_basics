import tkinter as tk

expression = ""


def input_number(number, input_field):
    global expression
    expression = expression + str(number)
    input_field.delete(first=0, last=20)
    input_field.insert(tk.END, expression)


def clear_input_field(input_field):
    global expression
    expression = ""
    input_field.delete(first=0, last=20)
    input_field.insert(tk.END, expression)


def evaluate(input_field):
    global expression
    try:
        result = str(eval(expression))
        input_field.delete(first=0, last=20)
        input_field.insert(tk.END, result)
        expression = ""
    except:
        expression = ""


def main():
    window = tk.Tk()
    window.title("Calculator")
    equation = "Enter data"
    input_field = tk.Entry(window, textvariable=equation, fg="black")
    input_field.place(height=100)
    input_field.grid(columnspan=4, ipadx=100, ipady=5)

    _1 = tk.Button(window, text='1', fg='white', bg='black', bd=0, command=lambda: input_number(1, input_field),
                   height=2,
                   width=7)
    _1.grid(row=2, column=0)
    _2 = tk.Button(window, text='2', fg='white', bg='black', bd=0, command=lambda: input_number(2, input_field),
                   height=2,
                   width=7)
    _2.grid(row=2, column=1)
    _3 = tk.Button(window, text='3', fg='white', bg='black', bd=0, command=lambda: input_number(3, input_field),
                   height=2,
                   width=7)
    _3.grid(row=2, column=2)
    _4 = tk.Button(window, text='4', fg='white', bg='black', bd=0, command=lambda: input_number(4, input_field),
                   height=2,
                   width=7)
    _4.grid(row=3, column=0)
    _5 = tk.Button(window, text='5', fg='white', bg='black', bd=0, command=lambda: input_number(5, input_field),
                   height=2,
                   width=7)
    _5.grid(row=3, column=1)
    _6 = tk.Button(window, text='6', fg='white', bg='black', bd=0, command=lambda: input_number(6, input_field),
                   height=2,
                   width=7)
    _6.grid(row=3, column=2)
    _7 = tk.Button(window, text='7', fg='white', bg='black', bd=0, command=lambda: input_number(7, input_field),
                   height=2,
                   width=7)
    _7.grid(row=4, column=0)
    _8 = tk.Button(window, text='8', fg='white', bg='black', bd=0, command=lambda: input_number(8, input_field),
                   height=2,
                   width=7)
    _8.grid(row=4, column=1)
    _9 = tk.Button(window, text='9', fg='white', bg='black', bd=0, command=lambda: input_number(9, input_field),
                   height=2,
                   width=7)
    _9.grid(row=4, column=2)
    _0 = tk.Button(window, text='0', fg='white', bg='black', bd=0, command=lambda: input_number(0, input_field),
                   height=2,
                   width=7)
    _0.grid(row=5, column=0)
    plus = tk.Button(window, text='+', fg='white', bg='black', bd=0, command=lambda: input_number('+', input_field),
                     height=2, width=7)
    plus.grid(row=2, column=3)
    minus = tk.Button(window, text='-', fg='white', bg='black', bd=0, command=lambda: input_number('-', input_field),
                      height=2, width=7)
    minus.grid(row=3, column=3)
    multiply = tk.Button(window, text='*', fg='white', bg='black', bd=0, command=lambda: input_number('*', input_field),
                         height=2, width=7)
    multiply.grid(row=4, column=3)
    divide = tk.Button(window, text='/', fg='white', bg='black', bd=0, command=lambda: input_number('/', input_field),
                       height=2, width=7)
    divide.grid(row=5, column=3)
    equal = tk.Button(window, text='=', fg='white', bg='black', bd=0, command=lambda: evaluate(input_field), height=2,
                      width=7)
    equal.grid(row=5, column=2)
    clear = tk.Button(window, text='Clear', fg='white', bg='black', bd=0,
                      command=lambda: clear_input_field(input_field),
                      height=2, width=7)
    clear.grid(row=5, column=1)

    window.mainloop()
