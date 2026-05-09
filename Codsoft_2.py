import tkinter as tk
from tkinter import messagebox

# ---------------- WINDOW ---------------- #

root = tk.Tk()
root.title("Modern GUI Calculator")
root.geometry("450x700")
bgm="#3a7d44"
root.configure(bg=bgm)
root.resizable(True, True)

# ---------------- FUNCTIONS ---------------- #

def calculate():

    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()

        if op == "+":
            result = num1 + num2

        elif op == "-":
            result = num1 - num2

        elif op == "*":
            result = num1 * num2

        elif op == "/":

            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return

            result = num1 / num2

        # UPDATE RESULT BOX
        result_var.set(str(result))

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")


def clear_fields():

    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_var.set("")

# ---------------- TITLE ---------------- #

title = tk.Label(
    root,
    text="Python Calculator",
    font=("Segoe UI", 24, "bold"),
    fg="#ffc100",
    bg=bgm
)

title.pack(pady=20)

# ---------------- MAIN FRAME ---------------- #

frame = tk.Frame(root, bg="#0d0c1d")
frame.pack(padx=20, pady=10)

# ---------------- INPUT 1 ---------------- #

label1 = tk.Label(
    frame,
    text="First Number",
    font=("Segoe UI", 12,"bold"),
    fg="#ffc100", #dark yellow
    bg="#0d0c1d"
)

label1.pack(pady=(20,5))

entry1 = tk.Entry(
    frame,
    font=("Segoe UI", 16),
    justify="center",
    width=20,
    bg="#f9fbb2",
    fg="black"
)

entry1.pack(ipady=8)

# ---------------- INPUT 2 ---------------- #

label2 = tk.Label(
    frame,
    text="Second Number",
    font=("Segoe UI", 12,"bold"),
    fg="#ffc100",
    bg="#0d0c1d" #black colour
)

label2.pack(pady=(20,5))

entry2 = tk.Entry(
    frame,
    font=("Segoe UI", 16),
    justify="center",
    width=20,
    bg="#f9fbb2",
    fg="black"
)

entry2.pack(ipady=8)

# ---------------- OPERATIONS ---------------- #

operation = tk.StringVar(value="+")

op_frame = tk.Frame(frame, bg="#0d0c1d")
op_frame.pack(pady=25)

for op in ["+", "-", "*", "/"]:

    rb = tk.Radiobutton(
        op_frame,
        text=op,
        variable=operation,
        value=op,

        indicatoron=0,   # Removes circle

        font=("Segoe UI", 18, "bold"),

        width=3,
        height=1,

        fg="white",
        bg="#444",

        selectcolor="#00b894",

        activebackground="#0d0c1d",
        activeforeground="#ffc100",

        bd=0,
        relief="ridge",

        cursor="hand2"
    )

    rb.pack(side="left", padx=10)

# ---------------- BUTTONS ---------------- #

btn_frame = tk.Frame(root, bg=bgm)
btn_frame.pack(pady=20)

calc_btn = tk.Button(
    btn_frame,
    text="Calculate",
    command=calculate,
    font=("Segoe UI", 13, "bold"),
    bg="#00b894",
    fg="white",
    width=12,
    height=2,
    bd=0
)

calc_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(
    btn_frame,
    text="Clear",
    command=clear_fields,
    font=("Segoe UI", 13, "bold"),
    bg="#d63031",
    fg="white",
    width=12,
    height=2,
    bd=0
)

clear_btn.grid(row=0, column=1, padx=10)

# ---------------- RESULT ---------------- #

result_label = tk.Label(
    root,
    text="Result",
    font=("Segoe UI", 14, "bold"),
    fg="#ffc100",
    bg=bgm
)

result_label.pack(pady=(20,5))

# STRING VARIABLE FOR RESULT
result_var = tk.StringVar()

result_box = tk.Entry(
    root,
    textvariable=result_var,
    font=("Segoe UI", 18, "bold"),
    justify="center",
    width=20,
    bd=3,
    fg="black",
    bg="#f9fbb2"
)

result_box.pack(ipady=3)

# ---------------- RUN APP ---------------- #

root.mainloop()
