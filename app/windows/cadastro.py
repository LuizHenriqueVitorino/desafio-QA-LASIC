import tkinter as tk
import json

def click():
    with open('app/models/user_model.json', 'r') as file:
        user = json.load(file)
        file.close()
    user['nome'] = nome.get()
    user['sobrenome'] = sobrenome.get()
    user['idade'] = idade.get()
    user['curso'] = curso.get()
    user['instituto'] = instituto.get()

    with open('usuarios.json', 'r')as file:
        data_base = json.load(file)
        file.close()
    data_base['usuarios'].append(user)
    data_base['quantidade'] = len(data_base['usuarios'])

    with open('usuarios.json', 'w') as file:
        json.dump(data_base, file, indent=4)
        file.close()

    # print(f"{user.nome} foi cadastrado!")

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