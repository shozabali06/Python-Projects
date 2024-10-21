import tkinter as tk
import string

def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Make your password at least 8 characters long.")

    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter (a-z).")

    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter (A-Z).")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Add at least one special character (e.g., !@#$%).")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one digit (0-9).")

    return score, suggestions

def on_password_change(*args):
    password = password_var.get()
    score, suggestions = check_password_strength(password)
    
    strength_labels = {
        0: "Very weak 😞",
        1: "Very weak 😞",
        2: "Weak 😐",
        3: "Moderate 🙂",
        4: "Strong 💪",
        5: "Strong 💪"
    }

    strength_label.config(text=strength_labels.get(score, "Unknown"))
    
    suggestions_label.config(text="\n".join(f"- {suggest}" for suggest in suggestions))

root = tk.Tk()
root.title("Password Strength Checker")

password_var = tk.StringVar()
password_var.trace_add("write", on_password_change)

password_entry = tk.Entry(root, textvariable=password_var, show='*')
password_entry.pack(pady=10)

strength_label = tk.Label(root, text="Strength will appear here")
strength_label.pack(pady=5)

suggestions_label = tk.Label(root, text="")
suggestions_label.pack(pady=5)

root.mainloop()
