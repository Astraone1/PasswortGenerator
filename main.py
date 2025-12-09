
import tkinter as tk
import random
import string

def generate_passwort():
    password = ""
    for i in range(12):
        password += random.choice(string.ascii_letters)
        label.config(text=password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x500")

label = tk.Label(root, text="Hier erscheint das Passwort")
label.pack()

button = tk.Button(root, text="Passwort generieren", command=generate_passwort)
button.pack()

########################








root.mainloop()