# Implemente a classe bicicleta, colocando limites maximos e minimos para os estados: veloc_atual, altura_cela e calibragem_pneus
# atraves de seus respectivos metodos. Altere os metodos, regular_cela, calibrar_pneus para permitirem as mudanças caso a bicileta esteja parada (veloc_atual = 0)

import time

class Bicicleta:
    def __init__(self, veloc):
        self.veloc_atual = veloc
        self.altura_cela = None
        self.calibragem_pneus = None

    def regular_cela(self):
        for i in range(3):
            time.sleep(3)
            print("Regulando celas, por favor, aguarde....")
        self.movimento()

    def calibrar_pneus(self):
        for i in range(3):
            time.sleep(3)
            print("Calibrando pneus, por favor, aguarde....")
        self.regular_cela()

    def movimento(self):
        direcao = 1
        while True:
            self.veloc_atual += direcao
            time.sleep(1)
            print(f"A velocidade atual da bicicleta é {self.veloc_atual} km/h")
            if self.veloc_atual == 5:
                direcao -= 1
                print(f"A velocidade atual da bicicleta é {self.veloc_atual} km/h")
            if self.veloc_atual == 0:
                self.calibrar_pneus()

resposta = Bicicleta(0)
resposta.movimento()

