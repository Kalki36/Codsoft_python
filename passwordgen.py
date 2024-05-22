import random
import string
import tkinter as tk

def generate_password():
    """Generate a random password of the specified length."""
    length = int(entry_length.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    label_password.config(text=f"Generated password: {password}")

root = tk.Tk()
root.title("Password Generator")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_length = tk.Label(frame, text="Enter the desired length of the password:")
label_length.grid(row=0, column=0, padx=(0, 10))

entry_length = tk.Entry(frame)
entry_length.grid(row=0, column=1)

button_generate = tk.Button(frame, text="Generate Password", command=generate_password)
button_generate.grid(row=1, column=0, columnspan=2, pady=(10, 0))

label_password = tk.Label(frame, text="")
label_password.grid(row=2, column=0, columnspan=2, pady=(10, 0))

root.mainloop()