#GUI version

import re
import tkinter as tk
from tkinter import messagebox

# Optional: list of common bad passwords
weak_words = ["password", "admin", "123456", "qwerty", "letmein"]

def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in weak_words:
        feedback.append("❌ Do not use common words like 'password' or 'admin'.")

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Use at least 8 characters.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Mix uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one special symbol.")

    if score == 4 and password.lower() not in weak_words:
        return "✅ Strong password!", feedback
    elif score >= 3:
        return "🟡 Moderate password.", feedback
    else:
        return "🔴 Weak password!", feedback

def on_check():
    password = entry.get()
    if not password:
        messagebox.showwarning("Empty", "Please enter a password.")
        return
    strength, suggestions = check_password_strength(password)
    messagebox.showinfo("Result", f"Strength: {strength}\n\n" + "\n".join(suggestions))

# GUI
root = tk.Tk()
root.title("Password Strength Tester")
root.geometry("400x250")

tk.Label(root, text="Enter your password:").pack(pady=10)
entry = tk.Entry(root, show="*", width=40)
entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=on_check).pack(pady=15)

root.mainloop()
