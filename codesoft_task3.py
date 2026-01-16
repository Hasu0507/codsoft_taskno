import tkinter as t
from tkinter import messagebox
import random
import string

# Random password
def generate_password():
    password_length = int(length_entry.get())

    if password_length <= 0:
        messagebox.showerror("Error", "Password length should be greater than 0")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(password_length))

    password_entry.delete(0, t.END)
    password_entry.insert(0, password)

# Main window
root = t.Tk()
root.title("Password Generator")

# password length
length_label = t.Label(root, text="Password Length:")
length_label.pack()

length_entry = t.Entry(root)
length_entry.pack()

# Generate password
generate_button = t.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Display the generated password
password_label = t.Label(root, text="Generated Password:")
password_label.pack()

password_entry = t.Entry(root, width=40)
password_entry.pack()
root.mainloop()
