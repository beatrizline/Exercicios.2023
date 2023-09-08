# Exercitando o processo de abstraçao, modele uma classe Relogio_Digital_Simples com seus estados e comportamentos.
# Crie a respectiva classe em python e depois crie 2 objetos, imprima os valores de seus atributos e execute os metodos criados.
# Recomendaçao: criar estados que possam ter seus valores alterados por seus metodos.

import time
class RelogioDigitalSimples:
    def __init__(self,hora,minuto):
        self.hora = hora
        self.minuto = minuto
        self.ligado = None
        self.desligado = None

    def liga(self):
        self.ligado = True
        self.desligado = False
        print("O relógio está ligado")

    def desliga(self):
        self.ligado = False
        self.desligado = True
        print("O relógio está desligado")

    def contador(self):
        if self.ligado == True:
            time.sleep(1)
            self.minuto += 1
            if self.minuto >= 60:
                self.hora += 1
                self.minuto = 0
            if self.hora >= 24:
                self.hora = 0
                self.minuto = 0
            print(f"{self.hora}:{self.minuto}")
        else:
            print("O relógio está desligado")

r = RelogioDigitalSimples(int(input("H: ")), int(input("M: ")))
r.liga()
while True:
    r.contador()


