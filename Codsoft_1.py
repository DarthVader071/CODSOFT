from tkinter import *
from tkinter import messagebox

# Main Window
root = Tk()
root.title("To-Do List")
root.geometry("500x500")
bgm="#3a7d44"
root.config(bg=bgm)
root.resizable(True ,True)

tasks = []

# ---------------- FUNCTIONS ---------------- #

def add_task():
    task = task_entry.get()

    if task != "":
        task_listbox.insert(END, task)
        task_entry.delete(0, END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task")


def delete_task():
    try:
        selected = task_listbox.curselection()
        task_listbox.delete(selected)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Please select a task")


def update_task():
    try:
        selected = task_listbox.curselection()

        new_task = task_entry.get()

        if new_task != "":
            task_listbox.delete(selected)
            task_listbox.insert(selected, new_task)

            task_entry.delete(0, END)
            save_tasks()
        else:
            messagebox.showwarning("Warning", "Enter updated task")

    except:
        messagebox.showwarning("Warning", "Select a task to update")


def save_tasks():
    tasks = task_listbox.get(0, END)

    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

            for task in tasks:
                task_listbox.insert(END, task.strip())

    except:
        pass


# ---------------- UI DESIGN ---------------- #

title = Label(
    root,
    text="TO-DO LIST",
    font=("Segoe UI", 20, "bold"),
    bg=bgm,
    fg="#ffc100"
)

title.pack(pady=10)

task_entry = Entry(
    root,
    font=("Segoe UI", 14),
    width=30
)

task_entry.pack(pady=10)

button_frame = Frame(root, bg=bgm)
button_frame.pack(pady=10)

add_btn = Button(
    button_frame,
    text="Add Task",
    width=12,
    bg="#4CAF50",
    fg="white",
    command=add_task
)

add_btn.grid(row=0, column=0, padx=5)

update_btn = Button(
    button_frame,
    text="Update Task",
    width=12,
    bg="#2196F3",
    fg="white",
    command=update_task
)

update_btn.grid(row=0, column=1, padx=5)

delete_btn = Button(
    button_frame,
    text="Delete Task",
    width=12,
    bg="#f44336",
    fg="white",
    command=delete_task
)

delete_btn.grid(row=0, column=2, padx=5)

# Listbox + Scrollbar
frame = Frame(root)
frame.pack(pady=20)

scrollbar = Scrollbar(frame)

task_listbox = Listbox(
    frame,
    width=48,
    height=15,
    font=("Segoe UI", 12),
    yscrollcommand=scrollbar.set,
    selectbackground="#a6a6a6"
)

scrollbar.config(command=task_listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)

task_listbox.pack(side=LEFT)

# Load Existing Tasks
load_tasks()

root.mainloop()
