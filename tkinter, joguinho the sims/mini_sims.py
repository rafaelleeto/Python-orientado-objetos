import tkinter as tk
import random

emprego = {"pintor" : "15",
           "físico" : "10",
           "mecânico" : "20" }


class Trabalho:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def inserir_trabalho(self, nome_trabalho, salario_nome):
        self.nome = nome_trabalho
        self.salario = salario_nome

    def pegar_salario(self):
        return self.salario


class Personagem:

    def __init__(self, nome):
        self.nome = nome
        self.dinheiro = 50
        self.fome = 100
        self.energia = 100
        self.higiene = 100
        self.trabalho: Trabalho = None
        self.mental = 100
        self.informacao = ""

    def trabalhar(self):
        assalto = random.randint(1, 10)
        if assalto == 1:
            self.dinheiro = 0
            self.mental = min(100, self.mental - 10)
            self.informacao = f"{self.nome} Foi assaltado e perdeu todo o dinheiro"
            return True
        else:
            self.dinheiro += self.trabalho.salario
            self.informacao = f"Você trabalhou e ganhou {self.dinheiro}"
            self.energia = max(0, self.energia - 10)
            self.higiene = max(0, self.higiene - 10)
            self.mental = max(0, self.mental - 10)
            return False

    def comer(self):
        if self.dinheiro < 10:
            self.informacao = f"{self.nome} Não tem dinheiro"
        else:
            self.informacao = "Você comeu!"
            self.dinheiro = min(100, self.dinheiro - 10)
            self.fome = min(100, self.fome - 10)

    def mostrar_propriedades(self):
        return (f"Nome : {self.nome} | Trabalho: {"" if self.trabalho is None else self.trabalho.nome} | Dinheiro: {self.dinheiro} | Fome: {self.fome} | Energia:\
    {self.energia} | Higiene: {self.higiene} | Mental: {self.mental}")

    def mostrar_informaçoes(self):
        return self.informacao

    def dormir(self):
        if self.higiene < 10:
            self.informacao = "Você não pode dormir sujo"
        else:
            self.informacao = "Você dormiu!"
            self.energia = min(100, self.energia + 100)
            self.fome = min(100, self.fome + 10)
            self.mental = min(100, self.mental + 100)

    def emprego(self, trabalho):
        self.trabalho = trabalho

    def tomar_banho(self):
        self.informacao = "Você tomou banho"
        self.higiene = min(100, self.higiene + 100)




if __name__ == "__main__":
    pass
