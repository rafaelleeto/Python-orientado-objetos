import tkinter as tk
import random


class Personagem:

    def __init__(self, nome):
        self.nome = nome
        self.dinheiro = 50
        self.fome = 100
        self.energia = 100
        self.higiene = 100
        self.trabalho = None
        self.mental = 100

    def trabalhar(self):
        assalto = random.randint(1, 10)
        if assalto == 1:
            self.dinheiro = 0
            self.mental = min(100, self.mental - 10)
            return ("VOCÊ FOI ASSALTADO E PERDEU TODO O DINHEIRO!")
        else:
            self.dinheiro += 10
            self.energia = max(0, self.energia - 10)
            self.higiene = max(0, self.higiene - 10)
            self.mental = max(0, self.mental - 10)

    def comer(self):
        if self.dinheiro < 10:
            print(f"{self.nome} não tem dinheiro")
        else:
            self.dinheiro = min(100, self.dinheiro - 10)
            self.fome = min(100, self.fome - 10)

    def mostrar_propriedades(self):
        return (f"Nome : {self.nome} | Dinheiro: {self.dinheiro} | Fome: {self.fome} | Energia:\
    {self.energia} | Higiene: {self.higiene} | Mental: {self.mental}")

    def dormir(self):
        if self.higiene < 10:
            print("Você não pode dormir sujo")
            pass
        else:
            self.energia = min(100, self.energia + 10)
            self.fome = min(100, self.fome + 10)
            self.mental = min(100, self.mental + 10)

    def tomar_banho(self):
        self.higiene = min(100, self.higiene + 10)


if __name__ == "__main__":
    personagem = Personagem("rafael")
    while True:
        opcao = int(input("""Digite \n1- Comer\n2-Trabalhar\n3-Descansar\n4-Tomar Banho
5- Mostrar Status\n"""))
        match opcao:

            case 1:
                personagem.comer()

            case 2:
                personagem.trabalhar()

            case 3:
                personagem.dormir()

            case 4:
                personagem.tomar_banho()

            case 5:
                personagem.mostrar_propriedades()

            case _:
                break
