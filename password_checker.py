import re
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.resizable(False, False)

label = tk.Label(root, text="Enter your password:", font=("Arial", 12))
label.pack(pady=10)

password_entry = tk.Entry(root, show='*', width=30, font=("Arial", 12))
password_entry.pack(pady=5)

def check_strength():
    password = password_entry.get()

    strong_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$"
    medium_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,}$"

    if re.match(strong_regex, password):
        result_label.config(text="Strength: STRONG 💪", fg="green")
    elif re.match(medium_regex, password):
        result_label.config(text="Strength: MEDIUM 🔐", fg="orange")
    else:
        result_label.config(text="Strength: WEAK ❌", fg="red")

check_button = tk.Button(root, text="Check Strength", command=check_strength, font=("Arial", 12))
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
