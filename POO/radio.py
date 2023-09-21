# No método ligar, atualizar o atributo ligado para True, o volume do rádio deverá ser
# inicializado com o volume mínimo do rádio. Se a antena estiver habilitada
# (antena_habilitada=True), a frequencia deverá ser inicializada com a frequencia da primeira
# estação de rádio definida no dicionário e a estação atual deverá ser inicializada com seu
# respectivo nome.


# No método desligar, mudar o estado para False, além de atualizar os atributos: volume,
# frequencia_atual e estação_atual para: None


# O método aumentar_volume deverá receber um atributo opcional com valor inicial igual a 1.
# Caso este valor seja passado na chamada do argumento, atualizar o volume com o valor do
# argumento (fazer a crítica para não ultrapassar os valores permitidos para o volume). Caso o
# argumento fique vazio na chamada, o atributo volume deverá ser incrementado de uma
# unidade. (Fazer a crítica para não ultrapassar o valor máximo permitido)


# Idem para o método: diminur_volume


# O método mudar_frequencia deverá receber um atributo opcional com valor inicial igual a 0.
# Caso seja passado um valor para a frequencia na chamada deste método, atualizar o atributo
# frequencia_atual para o valor passado no argumento. Se o valor da frequencia estiver
# presente no dicionário, atualizar o atributo: estação_atual com o nome da respectiva
# frequencia que se encontra no dicionário, caso contrário atualizar com o valor: ‘estação
# inexistente’. Caso este método seja chamado sem argumentos, atualizar a frequencia_atual
# com a frequência referente ao próximo elemento do dicionário e atualizar o atributo:
# estação_atual com seu respectivo nome. Se a frequencia atual for igual ao último elemento do
# dicionário, mudar os atributos: frequencia e estação para os respectivos valores referentes ao
# primeiro elemento do dicionário.


# Criar pelo menos 3 objetos e testar os métodos implementados.

class RadioFM:
    def __init__(self, vol_max, estacoes):
        self.volume_min = 0
        self.volume_max = vol_max
        self.freq_min = 88
        self.freq_max = 108
        self.estacoes = estacoes
        self.volume = None
        self.ligado = False
        self.estacao_atual = None
        self.frequencia_atual = None
        self.antena_habilitada = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            self.volume = self.volume_min
            if self.antena_habilitada and self.estacoes:
                frequencia_inicial = min(self.estacoes.keys())
                self.frequencia_atual = frequencia_inicial
                self.estacao_atual = self.estacoes[frequencia_inicial]
                print(f"O rádio foi ligado. Volume: {self.volume}, Estação: {self.estacao_atual} ({self.frequencia_atual} FM).")
            else:
                print(f"O rádio foi ligado. Volume: {self.volume}.")
        else:
            print("O rádio já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.volume = None
            self.frequencia_atual = None
            self.estacao_atual = None
            print("O rádio foi desligado.")
        else:
            print("O rádio já está desligado.")

    def aumentar_volume(self, incremento=1):
        if self.ligado:
            novo_volume = self.volume + incremento
            if novo_volume > self.volume_max:
                print("Volume no máximo.")
                self.volume = self.volume_max
            else:
                self.volume = novo_volume
                print(f"Volume aumentado para {self.volume}.")
        else:
            print("Ligue o rádio primeiro.")

    def diminuir_volume(self, decremento=1):
        if self.ligado:
            novo_volume = self.volume - decremento
            if novo_volume < self.volume_min:
                print("Volume no mínimo.")
                self.volume = self.volume_min
            else:
                self.volume = novo_volume
                print(f"Volume diminuído para {self.volume}.")
        else:
            print("Ligue o rádio primeiro.")

    def mudar_frequencia(self, frequencia=None):
        if self.ligado:
            if frequencia is not None:
                self.frequencia_atual = frequencia
                self.estacao_atual = self.estacoes.get(frequencia, 'Estação inexistente')
            else:
                if self.frequencia_atual is None:
                    frequencia_inicial = min(self.estacoes.keys())
                    self.frequencia_atual = frequencia_inicial
                    self.estacao_atual = self.estacoes[frequencia_inicial]
                else:
                    frequencias_ordenadas = sorted(self.estacoes.keys())
                    index_atual = frequencias_ordenadas.index(self.frequencia_atual)
                    if index_atual < len(frequencias_ordenadas) - 1:
                        self.frequencia_atual = frequencias_ordenadas[index_atual + 1]
                    else:
                        # Chegou ao último elemento, volta para o primeiro
                        self.frequencia_atual = frequencias_ordenadas[0]
                    self.estacao_atual = self.estacoes[self.frequencia_atual]
            print(f"Sintonizado em {self.estacao_atual} ({self.frequencia_atual} FM).")
        else:
            print("Ligue o rádio primeiro.")


# Dicionário de estações
estacoes = {89.5: 'Cocais', 91.5: 'Mix', 94.1: 'Boa', 99.1: 'Clube'}

# Criar três rádios com volumes máximos diferentes
radio1 = RadioFM(10, estacoes)
radio2 = RadioFM(15, estacoes)
radio3 = RadioFM(5, estacoes)

# Testar os métodos
radio1.ligar()
radio1.aumentar_volume()
radio1.mudar_frequencia()
radio1.mudar_frequencia()
radio1.diminuir_volume(2)
radio1.desligar()

print("\n")

radio2.ligar()
radio2.aumentar_volume(3)
radio2.mudar_frequencia()
radio2.mudar_frequencia()
radio2.diminuir_volume()
radio2.mudar_frequencia(94.1)
radio2.mudar_frequencia()
radio2.desligar()

print("\n")

radio3.ligar()
radio3.aumentar_volume(2)
radio3.mudar_frequencia()
radio3.mudar_frequencia()
radio3.diminuir_volume()
radio3.mudar_frequencia()
radio3.desligar()
