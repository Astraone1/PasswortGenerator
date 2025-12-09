import tkinter as tk
import random
import string

def generate_password(laenge=12):
    buchstaben = string.ascii_letters  # a-zA-Z
    zahlen = string.digits             # 0-9
    zeichen = buchstaben + zahlen
    return ''.join(random.choice(zeichen) for _ in range(laenge))

def generate_and_display():
    password = generate_password(12)
    label.config(text=password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x500")

label = tk.Label(root, text="Hier erscheint das Passwort", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root, text="Passwort generieren", command=generate_and_display)
button.pack(pady=10)

root.mainloop()