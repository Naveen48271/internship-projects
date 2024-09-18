import tkinter as tk
from tkinter import messagebox

# Function to update the display when a button is pressed
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to clear the display
def button_clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        messagebox.showerror("Error", "Invalid input")

# Creating the main window
root = tk.Tk()
root.title("Calculator")

# Creating an Entry widget for the display
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Defining buttons
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '.', '=', '+'
]

# Adding buttons to the grid
row_value = 1
col_value = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=9, command=button_equal).grid(row=row_value, column=col_value, columnspan=2)
    elif button == 'C':
        tk.Button(root, text=button, width=9, command=button_clear).grid(row=row_value, column=col_value, columnspan=2)
    else:
        tk.Button(root, text=button, width=9, command=lambda value=button: button_click(value)).grid(row=row_value, column=col_value)
    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

# Adding the clear button
tk.Button(root, text='C', width=9, command=button_clear).grid(row=row_value, column=0)

# Running the application
root.mainloop()
