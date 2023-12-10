import random
import string
import tkinter as tk

def generate_random_id(length=10):
    characters = string.ascii_lowercase + string.digits
    random_id = ''.join(random.choice(characters) for i in range(length))
    return random_id

def addRegister(window=None, name=''):
    register_label = tk.Label(window, text=name)
    register_label.pack(padx=10)

    register = tk.Entry(window,)
    register.pack(padx=10, pady=10)

    return register