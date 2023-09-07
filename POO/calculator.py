# Implementar uma classe que represente uma calculadora simples contendo as quatro operações básicas.
# Execute através da criação e manipulação de objetos.

class Calculadora:
    estado = 'desligado'
    numero1 = None
    numero2 = None
    operacao = None
    resultado = None


    def ligar(self):
        self.estado = 'ligado'
        self.resetar()
        print(f'Calculadora ligada!')

    def desligado(self):
        self.estado = 'desligado'
        self.number1 = None
        self.number2 = None
        self.operation = None
        self.result = None
        print(f'Calculadora desligada!')


    def resetar(self):
        if self.estado == 'ligado':
            self.numero1 = 0
            self.numero2 = 0
            self.operacao = None
            self.resultado = 0
            print(self.resultado)
        else:
            print("Calculadora desligada!")

    def somar(self):
        if self.estado == 'ligado':
            self.number1 = float(input("n1: "))
            self.number2 = float(input("n2: "))
            self.result = self.number1 + self.number2
            print(f'A soma de {self.number1} + {self.number2} é {self.result}')
        else:
            print("Calculadora desligada")


    def subtracao(self):
        if self.estado == 'ligado':
            self.number1 = float(input("n1: "))
            self.number2 = float(input("n2: "))
            self.result = self.number1 - self.number2
            print(f'A subtração de {self.number1} - {self.number2} é {self.result}')
        else:
            print("Calculadora desligada")


    def multip(self):
        if self.estado == 'ligado':
            self.number1 = float(input("n1: "))
            self.number2 = float(input("n2: "))
            self.result = self.number1 * self.number2
            print(f'A multiplicação de {self.number1} * {self.number2} é {self.result}')
        else:
            print("Calculadora desligada")


    def divisao(self):
        if self.estado == 'ligado':
            self.number1 = float(input("n1: "))
            self.number2 = float(input("n2: "))
            self.result = self.number1 / self.number2
            print(f'A divisão de {self.number1} / {self.number2} é {self.result}')
        else:
            print("Calculadora desligada")


c1 = Calculadora()
c1.ligar()
while True:
    prosseguir = print("Digite qual operação você deseja utilizar.")
    prosseguir1 = input(
        "S para soma, SUB para subtração, M para multiplicação, D para divisão, EXIT para sair: ").upper()
    if prosseguir1 == 'S':
        c1.somar()
    elif prosseguir1 == 'SUB':
        c1.subtracao()
    elif prosseguir1 == 'M':
        c1.multip()
    elif prosseguir1 == 'D':
        c1.divisao()
    elif prosseguir1 == 'EXIT':
        tentativa = input("Tem certeza que deseja sair? Podemos prosseguir com o cálculo (S - sim, N - não): ").upper()
        if tentativa == 'S':
            c1.ligar()
        if tentativa == 'N':
            print('Calculadora desligada!')
            break
    else:
        print('Esta entrada não é válida. Tente novamente')


