import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operand = operation.get()
        
        if operand == "+":
            answer = num1 + num2
        elif operand == "-":
            answer = num1 - num2
        elif operand == "*":
            answer = num1 * num2
        elif operand == "/":
            answer = num1 / num2
        elif operand == "%":
            answer = num1 % num2
        elif operand == "**":
            answer = num1 ** num2
        else:
            messagebox.showerror("Error", "Invalid operation")
            return
        
        result_var.set(answer)
        entry1.delete(0, tk.END)
        entry1.insert(0, str(answer))
        entry2.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Invalid input")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def reset():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_var.set("")

root = tk.Tk()
root.title("Basic Calculator")

frame = tk.Frame(root)
frame.pack(pady=10)

label1 = tk.Label(frame, text="Enter the first number:")
label1.grid(row=0, column=0, padx=5, pady=5)

entry1 = tk.Entry(frame)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = tk.Label(frame, text="Enter the second number:")
label2.grid(row=1, column=0, padx=5, pady=5)

entry2 = tk.Entry(frame)
entry2.grid(row=1, column=1, padx=5, pady=5)

label3 = tk.Label(frame, text="Enter the operation (+, -, *, /, %, **):")
label3.grid(row=2, column=0, padx=5, pady=5)

operation = tk.Entry(frame)
operation.grid(row=2, column=1, padx=5, pady=5)

result_var = tk.StringVar()
result_label = tk.Label(frame, text="Result:")
result_label.grid(row=3, column=0, padx=5, pady=5)

result_entry = tk.Entry(frame, textvariable=result_var, state='readonly')
result_entry.grid(row=3, column=1, padx=5, pady=5)

calculate_button = tk.Button(frame, text="Calculate", command=calculate)
calculate_button.grid(row=4, column=0, padx=5, pady=5)

reset_button = tk.Button(frame, text="Reset", command=reset)
reset_button.grid(row=4, column=1, padx=5, pady=5)

root.mainloop()





import tkinter as tk
from tkinter import font as tkfont

# Initialize the main window
root = tk.Tk()
root.title("Colorful Calculator")

# Set the main window size
root.geometry("400x500")
root.resizable(False, False)

# Define colors inspired by the provided image
colors = {
    "bg": "#4c14c4",  
    "button_bg": "#a13308",  
    "button_fg": "#FFFFFF",  # White
    "entry_bg": "#FFFFFF",  # White
    "entry_fg": "#000000",  # Black
    "button_active_bg": "#0e0e82"  # 
}

# Define font styles
entry_font = tkfont.Font(family="Times new roman", size=34)
button_font = tkfont.Font(family="Helvetica", size=18, weight="bold")

# Function to update the entry field
def update_entry(text):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + text)

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Create entry widget
entry = tk.Entry(root, font=entry_font, bg=colors["entry_bg"], fg=colors["entry_fg"], borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="we")

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Create buttons dynamically
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, font=button_font, bg=colors["button_bg"], fg=colors["button_fg"],
                        activebackground=colors["button_active_bg"], command=evaluate_expression)
    elif text == 'C':
        btn = tk.Button(root, text=text, font=button_font, bg=colors["button_bg"], fg=colors["button_fg"],
                        activebackground=colors["button_active_bg"], command=clear_entry)
    else:
        btn = tk.Button(root, text=text, font=button_font, bg=colors["button_bg"], fg=colors["button_fg"],
                        activebackground=colors["button_active_bg"], command=lambda t=text: update_entry(t))
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Configure row and column weights for resizing
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Set the background color
root.configure(bg=colors["bg"])

# Start the main event loop
root.mainloop()













import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operand = operation.get()
        
        if operand == "+":
            answer = num1 + num2
        elif operand == "-":
            answer = num1 - num2
        elif operand == "*":
            answer = num1 * num2
        elif operand == "/":
            answer = num1 / num2
        elif operand == "%":
            answer = num1 % num2
        elif operand == "**":
            answer = num1 ** num2
        else:
            messagebox.showerror("Error", "Invalid operation")
            return
        
        result_var.set(answer)
        entry1.delete(0, tk.END)
        entry1.insert(0, str(answer))
        entry2.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Invalid input")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def reset():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_var.set("")

root = tk.Tk()
root.title("Colorful Basic Calculator")

root.configure(bg="#e0f7fa")

frame = tk.Frame(root, bg="#e0f7fa")
frame.pack(pady=20)

label1 = tk.Label(frame, text="Enter the first number:", font=("Arial", 14), bg="#e0f7fa")
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = tk.Entry(frame, font=("Arial", 14))
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(frame, text="Enter the second number:", font=("Arial", 14), bg="#e0f7fa")
label2.grid(row=1, column=0, padx=10, pady=10)

entry2 = tk.Entry(frame, font=("Arial", 14))
entry2.grid(row=1, column=1, padx=10, pady=10)

label3 = tk.Label(frame, text="Enter the operation (+, -, *, /, %, **):", font=("Arial", 14), bg="#e0f7fa")
label3.grid(row=2, column=0, padx=10, pady=10)

operation = tk.Entry(frame, font=("Arial", 14))
operation.grid(row=2, column=1, padx=10, pady=10)

result_var = tk.StringVar()
result_label = tk.Label(frame, text="Result:", font=("Arial", 14), bg="#e0f7fa")
result_label.grid(row=3, column=0, padx=10, pady=10)

result_entry = tk.Entry(frame, textvariable=result_var, font=("Arial", 14), state='readonly')
result_entry.grid(row=3, column=1, padx=10, pady=10)

calculate_button = tk.Button(frame, text="Calculate", font=("Arial", 14), command=calculate, bg="#00796b", fg="white")
calculate_button.grid(row=4, column=0, padx=10, pady=20)

reset_button = tk.Button(frame, text="Reset", font=("Arial", 14), command=reset, bg="#00796b", fg="white")
reset_button.grid(row=4, column=1, padx=10, pady=20)

root.mainloop()


