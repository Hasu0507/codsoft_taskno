import tkinter as t

def add_task():
    task = task_entry.get()
    if task:
        task_lb.insert(t.END, task)
        task_entry.delete(0, t.END)

def remove_task():
    sd_task_index = task_lb.curselection()
    if sd_task_index:
        task_lb.delete(sd_task_index)

# Main window
root = t.Tk()
root.title("TO-D0 LIST")
root.geometry("300x310+400+100")

# Listbox to display tasks
task_lb = t.Listbox(root)
task_lb.pack(pady=10)

# Entry widget to add new tasks
task_entry = t.Entry(root)
task_entry.pack(pady=10)

# Add and Remove buttons
add_button = t.Button(root, text="Add Task", command=add_task)
remove_button = t.Button(root, text="Remove Task", command=remove_task)
add_button.pack()
remove_button.pack()

# Start the Tkinter main loop
root.mainloop()
