import tkinter as tk


# Function to update the entry widget with the pressed button value
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END) #Perintah ini digunakan untuk melakuakan delete pada bagian tombol yang ditekan 
    entry.insert(tk.END, current + str(value))


# Function to clear the entry widget
def button_clear():
    entry.delete(0, tk.END)


# Function to evaluate the expression
def button_equal():
    try:
        result = eval(entry.get())  # This evaluates the expression entered
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


# Initialize the main window
root = tk.Tk()
root.title("Basic Calculator")

# Create the entry widget for showing the current calculation
entry = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=2, relief='solid', justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Create button widgets and place them in a grid
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Loop to create the buttons dynamically
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=button_equal)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda value=text: button_click(value))
    button.grid(row=row, column=col)

# Clear button
clear_button = tk.Button(root, text="C", width=5, height=2, font=('Arial', 18), command=button_clear)
clear_button.grid(row=5, column=0, columnspan=4)

# Run the main loop to display the GUI
root.mainloop()
