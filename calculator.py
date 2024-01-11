
import tkinter as tk

def calculator():
    # Define basic window and display
    root = tk.Tk()
    root.title("Basic Calculator")
    display = tk.Entry(root, width=40, borderwidth=30, font=("Arial", 20))  

    display.grid(row=0, columnspan=4)

    # Define operand and operator variables
    num1 = 0
    operator = ""

    
    def button_click(value):
        """Define button functions"""
        nonlocal num1, operator
        if value.isdigit():
            current_text = display.get()
            display.delete(0, tk.END)
            display.insert(0, current_text + value)
        elif value in "+-*/":
            num1 = float(display.get())
            operator = value
            display.delete(0, tk.END)
        elif value == "=":
            num2 = float(display.get())
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    result = 0
                else:
                    result = num1 / num2
            else:
                result = "Invalid operator"
            display.delete(0, tk.END)
            display.insert(0, result)
            num1 = 0
            operator = ""
        elif value == "C":
            display.delete(0, tk.END)
            num1 = 0
            operator = ""

    # Create and arrange buttons
    button_list = [
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "0", ".", "C", "+",
        "="
    ]

    row = 1
    col = 0
    for button_text in button_list:
        button = tk.Button(root, text=button_text, command=lambda char=button_text: button_click(char))
        button.grid(row=row, column=col, sticky="nsew")
        col += 1
        if col > 3:
            col = 0
            row += 1

    root.mainloop()

calculator()
