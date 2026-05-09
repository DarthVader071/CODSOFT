from tkinter import *
from tkinter import messagebox
import random
import string

# ---------------- MAIN WINDOW ---------------- #

root = Tk()
root.title("Random Password Generator")
root.geometry("600x550")
background="#3a7d44"
root.config(bg=background)
root.resizable(True, True)

# ---------------- FUNCTIONS ---------------- #

def generate_password():

    password = ""

    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showwarning(
                "Warning",
                "Password length must be at least 4"
            )
            return

        # Character sets
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        # Ensure strong password
        password += random.choice(lowercase)
        password += random.choice(uppercase)
        password += random.choice(digits)
        password += random.choice(symbols)

        # Remaining characters
        all_characters = (
            lowercase +
            uppercase +
            digits +
            symbols
        )

        for i in range(length - 4):
            password += random.choice(all_characters)

        # Shuffle password
        password_list = list(password)
        random.shuffle(password_list)

        password = "".join(password_list)

        # Display password
        result_entry.delete(0, END)
        result_entry.insert(0, password)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter a valid number"
        )


def copy_password():

    password = result_entry.get()

    if password == "":
        messagebox.showwarning(
            "Warning",
            "Generate a password first"
        )
    else:
        root.clipboard_clear()
        root.clipboard_append(password)

        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard"
        )


def clear_fields():

    length_entry.delete(0, END)
    result_entry.delete(0, END)


# ---------------- TITLE ---------------- #

title_label = Label(
    root,
    text="PASSWORD GENERATOR",
    font=("Segoe UI", 24, "bold"),
    bg=background,
    fg="#ffc100"
)

title_label.pack(pady=20)

# ---------------- LENGTH INPUT ---------------- #

length_label = Label(
    root,
    text="Enter Password Length:",
    font=("Segoe UI", 14, "bold"),
    bg=background,
    fg="#ffc100"
)

length_label.pack(pady=10)

length_entry = Entry(
    root,
    font=("Segoe UI", 14),
    width=20,
    justify="center",
    bd=3
)

length_entry.pack(pady=5)

# ---------------- GENERATE BUTTON ---------------- #

generate_button = Button(
    root,
    text="Generate Password",
    font=("Segoe UI", 13, "bold"),
    bg="#f9fbb2", #yellow
    fg="#4CAF50",
    width=20,
    command=generate_password
)

generate_button.pack(pady=20)

# ---------------- RESULT SECTION ---------------- #

result_label = Label(
    root,
    text="Generated Password:",
    font=("Segoe UI", 14,"bold"),
    fg="#ffc100",
    bg=background
)

result_label.pack(pady=10)

result_entry = Entry(
    root,
    font=("Segoe UI", 14),
    width=30,
    justify="center",
    bd=3
)

result_entry.pack(pady=5)

# ---------------- BUTTON FRAME ---------------- #

button_frame = Frame(root, bg=background)
button_frame.pack(pady=20)

copy_button = Button(
    button_frame,
    text="Copy",
    font=("Segoe UI", 12, "bold"),
    bg="#2196F3",
    fg="white",
    width=10,
    command=copy_password
)

copy_button.grid(row=0, column=0, padx=10)

clear_button = Button(
    button_frame,
    text="Clear",
    font=("Segoe UI", 12, "bold"),
    bg="#f44336",
    fg="white",
    width=10,
    command=clear_fields
)

clear_button.grid(row=0, column=1, padx=10)

# ---------------- FOOTER ---------------- #

footer_label = Label(
    root,
    text="Python Tkinter Password Generator",
    font=("Segoe UI", 10),
    bg=background,
    fg="white"
)

footer_label.pack(side=BOTTOM, pady=10)

# ---------------- RUN APPLICATION ---------------- #

root.mainloop()
