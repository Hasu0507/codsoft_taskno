import tkinter as t

def button_click(number):
    current = entry.get()
    entry.delete(0, t.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, t.END)

def button_equal():
    current = entry.get()
    try:
        result = eval(current)
        entry.delete(0, t.END)
        entry.insert(0, result)
    except:
        entry.delete(0, t.END)
        entry.insert(0, "Error")

# Main window
root = t.Tk()
root.title("Calculator")

# Display input and results
entry = t.Entry(root, width=22, borderwidth=6, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

rval = 1
cval = 0

for button in buttons:
    if button == '=':
        t.Button(
            root, text=button, padx=20, pady=20,
            command=button_equal
        ).grid(row=rval, column=cval)
    else:
        t.Button(
            root, text=button, padx=20, pady=20,
            command=lambda b=button: button_click(b)
        ).grid(row=rval, column=cval)

    cval += 1
    if cval > 3:
        cval = 0
        rval += 1

# Clear button
cr_button = t.Button(root, text="C", padx=20, pady=20, command=button_clear)
cr_button.grid(row=rval, column=cval)

# Start the GUI main loop
root.mainloop()
