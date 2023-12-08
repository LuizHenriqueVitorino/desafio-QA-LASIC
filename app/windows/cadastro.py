import tkinter as tk

def click():
    print(f"{nome.get()} foi cadastrado!")

def addRegister(name=''):
    register_label = tk.Label(window, text=name)
    register_label.pack(padx=10)

    register = tk.Entry(window)
    register.pack(padx=10, pady=10)

    return register

window = tk.Tk()

window.geometry("500x800")

metodo_label = tk.Label(window, text="CADASTRO")
metodo_label.pack(padx=10, pady=10)

nome      = addRegister("NOME")
sobrenome = addRegister("SOBRENOME")
idade     = addRegister("IDADE")
curso     = addRegister("CURSO")
instituto = addRegister("INSTITUIÇÃO")

register_email = tk.Label(window,)

register_button = tk.Button(window, text="CADASTRAR", command=click)
register_button.pack(padx=10, pady=10)


window.mainloop()