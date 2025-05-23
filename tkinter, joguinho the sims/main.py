import tkinter as tk
from mini_sims import Personagem

personagem = Personagem("Jose")


def atualizar_label():
    label.config(text=personagem.mostrar_propriedades())


def comer():
    personagem.comer()
    atualizar_label()


def trabalhar():
    personagem.trabalhar()
    atualizar_label()


def dormir():
    personagem.dormir()
    atualizar_label()


def tomar_banho():
    personagem.tomar_banho()
    atualizar_label()


if __name__ == "__main__":

    janela = tk.Tk()
    janela.title("Minha Janela")
    janela.geometry("800x600")

    label = tk.Label(
        janela, text=personagem.mostrar_propriedades(), font=("Arial", 15))
    label.pack(padx=10, pady=10)

    botao = tk.Button(janela, text="Comer", command=comer)
    botao.pack(padx=10, pady=10)

    botao = tk.Button(janela, text="Trabalhar", command=trabalhar)
    botao.pack(padx=10, pady=10)

    botao = tk.Button(janela, text="Descansar 😄", command=dormir)
    botao.pack(padx=10, pady=10)

    botao = tk.Button(janela, text="Tomar banho", command=tomar_banho)
    botao.pack(padx=10, pady=10)

    janela.mainloop()
