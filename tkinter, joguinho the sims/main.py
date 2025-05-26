import tkinter as tk
from mini_sims import Personagem, Trabalho

personagem = Personagem("Jose")


def atualizar_label():
    label.config(text=personagem.mostrar_propriedades())
    informacao.config(text=personagem.mostrar_informaçoes())


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


def escolher_trabalho(emprego):
    novo_trabalho = Trabalho(emprego, 0)
    personagem.trabalho = novo_trabalho
    print(personagem.trabalho)
    if emprego == "pintor":
        novo_trabalho.inserir_trabalho(emprego, 20)

    if emprego == "físico":
        novo_trabalho.inserir_trabalho(emprego, 40)

    if emprego == "mecânico":
        novo_trabalho.inserir_trabalho(emprego, 50)

    atualizar_label()


def abrir_janela():
    subjanela = tk.Toplevel(janela)
    subjanela.title("Trabalho")
    subjanela.geometry("600x400")

    botao = tk.Button(subjanela, text="pintor",
                      command=lambda: escolher_trabalho("pintor"))
    botao.pack(padx=10, pady=10)
    botao = tk.Button(subjanela, text="físico",
                      command=lambda: escolher_trabalho("físico"))
    botao.pack(padx=10, pady=10)
    botao = tk.Button(subjanela, text="mecânico",
                      command=lambda: escolher_trabalho("mecânico"))
    botao.pack(padx=10, pady=10)
    atualizar_label()
    subjanela.mainloop()


if __name__ == "__main__":

    janela = tk.Tk()
    janela.title("Minha Janela")
    janela.geometry("1000x800")

    label = tk.Label(
        janela, text=personagem.mostrar_propriedades(), font=("Arial", 15))
    label.pack(padx=10, pady=10)

    informacao = tk.Label(
        janela, text=personagem.mostrar_informaçoes(), font=("Arial", 15))
    informacao.pack(padx=10, pady=10)

    botao = tk.Button(janela, text="Escolher emprego", command=abrir_janela)
    botao.pack(padx=10, pady=10)

    botao = tk.Button(janela, text="Comer", command=comer)
    botao.pack(padx=10, pady=10)

    botao = tk.Button(janela, text="Trabalhar", command=trabalhar)
    botao.pack(padx=10, pady=10)

    botao = tk.Button(janela, text="Descansar ", command=dormir)
    botao.pack(padx=10, pady=10)

    botao = tk.Button(janela, text="Tomar banho", command=tomar_banho)
    botao.pack(padx=10, pady=10)

    janela.mainloop()
