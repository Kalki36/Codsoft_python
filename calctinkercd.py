import tkinter as tk

def cal():
    n1 = float(entry_n1.get())
    o = entry_o.get()
    n2 = float(entry_n2.get())
    result = cal_fun(n1, n2, o)
    label_result.config(text=f"={result}")

def cal_fun(n1, n2, o):
    if o == '+':
        result = n1 + n2
    elif o == '-':
        result = n1 - n2
    elif o == '*':
        result = n1 * n2
    elif o == '/':
        if n2!= 0:
            result = n1 / n2
        else:
            raise ValueError('Division by zero is not allowed')
    elif o == '^':
        result = n1 ** n2
    else:
        raise ValueError('Invalid operator')

    if result.is_integer():
        result = int(result)

    return result

root = tk.Tk()
root.title("Calculator")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_n1 = tk.Label(frame, text="Enter first number:")
label_n1.grid(row=0, column=0, padx=(0, 10))
entry_n1 = tk.Entry(frame)
entry_n1.grid(row=0, column=1)

label_o = tk.Label(frame, text="Enter operator (+,-,*,/,^):")
label_o.grid(row=1, column=0, padx=(0, 10))
entry_o = tk.Entry(frame)
entry_o.grid(row=1, column=1)

label_n2 = tk.Label(frame, text="Enter second number:")
label_n2.grid(row=2, column=0, padx=(0, 10))
entry_n2 = tk.Entry(frame)
entry_n2.grid(row=2, column=1)

button_cal = tk.Button(frame, text="Calculate", command=cal)
button_cal.grid(row=3, column=0, columnspan=2, pady=(10, 0))

label_result = tk.Label(frame, text="")
label_result.grid(row=4, column=0, columnspan=2, pady=(10, 0))

root.mainloop()