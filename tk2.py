import tkinter as tk
from tkinter import messagebox

def add_number():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1+num2
        messagebox.showinfo("Result", result)
    except ValueError:
        messagebox.showerror("Error", "please enter valid numbers.")
        
        
def sub_number():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1-num2
        messagebox.showinfo("Result", result)
    except ValueError:
        messagebox.showerror("Error", "please enter valid numbers.")
        
        
def multi_number():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1*num2
        messagebox.showinfo("Result", result)
    except ValueError:
        messagebox.showerror("Error", "please enter valid numbers.")
        
        
def div_number():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1/num2
        messagebox.showinfo("Result", result)
    except ValueError:
        messagebox.showerror("Error", "please enter valid numbers.")
        
root = tk.Tk()
root.title("simple adder")
tk.Label(root,text="number 1:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root,text="number 2:").grid(row=1, column=0, padx=10, pady=10)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

add_button = tk.Button(root, text="Add", command=add_number )
add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

div_button = tk.Button(root, text="div", command=div_number )
div_button.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

sub_button = tk.Button(root, text="sub", command=sub_number )
sub_button.grid(row=2, column=2, columnspan=2, padx=10, pady=10)

multi_button = tk.Button(root, text="multi", command=multi_number )
multi_button.grid(row=2, column=4, columnspan=2, padx=10, pady=10)


root.mainloop()