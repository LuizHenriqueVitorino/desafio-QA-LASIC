import tkinter as tk
from utils.utils import *

window = tk.Tk()
window.geometry("500x800")

titulo = tk.Label(window, text="PESQUISAR USUÁRIO")
titulo.pack()

id = addRegister(window=window, name="Digite o ID:")

button = tk.Button(window, text="PESQUISAR")
button.pack()

window.mainloop()