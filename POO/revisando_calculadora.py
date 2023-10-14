
# Implementar uma classe que represente uma calculadora simples contendo as quatro operações básicas.
# Execute através da criação e manipulação de objetos.

# Treinei novamente o desafio sobre fazer uma calculadora, compreendi um pouco mais poo e to aprendendo...finalmente
# bom, dessa vez tentei tornar o mais simples possivel a implementaçao do codigo,
# utilizei construtores e atributos de instancia e opcionais

class Calculator:
    def __init__(self, valor_um=0, valor_dois=0, estado=True):
        self.valor_um = valor_um
        self.valor_dois = valor_dois
        self.estado = estado


    def desligada(self):
        if not self.estado:
            self.valor_um = None
            self.valor_dois = None

    def ligar(self):
        if self.estado:
            self.resetar()
            print("Calculadora ligada!")
        else:
            print("Calculadora desligada!")

    # a funcao resetar, retornara todos os valores do atributo de classe como zero
    def resetar(self):
        if self.estado:
            self.valor_um = 0
            self.valor_dois = 0
            print(self.valor_um)
        else:
            print("Calculadora desligada!")

    def somar(self):
        if self.estado:
            self.valor_um = float(input("n1: "))
            self.valor_dois = float(input("n2: "))
            self.resultado = self.valor_um + self.valor_dois
            print(f"A soma de {self.valor_um} + {self.valor_dois} é {self.resultado}")
        else:
            print("Por gentileza, ligue sua calculadora")

    def subtracao(self):
        if self.estado:
            self.valor_um = float(input("n1: "))
            self.valor_dois = float(input("n2: "))
            self.resultado = self.valor_um - self.valor_dois
            print(f"A subtração de {self.valor_um} - {self.valor_dois} é {self.resultado}")
        else:
            print("Por gentileza, ligue sua calculadora")

    def multiplicacao(self):
        if self.estado:
            self.valor_um = float(input("n1: "))
            self.valor_dois = float(input("n2: "))
            self.resultado = self.valor_um * self.valor_dois
            print(f"A multiplicação de {self.valor_um} * {self.valor_dois} é {self.resultado}")
        else:
            print("Por gentileza, ligue sua calculadora")

    def divisao(self):
        if self.estado:
            self.valor_um = float(input("n1: "))
            self.valor_dois = float(input("n2: "))
            self.resultado = self.valor_um / self.valor_dois
            print(f"A divisão de {self.valor_um} /  {self.valor_dois} é {self.resultado}")
        else:
            print("Por gentileza, ligue sua calculadora")

    def principal(self):

        while True:
            print(f'(+) - somar (-)-subtrair (*)-multiplicar (/)-dividir (c)-resetar (s)-sair')
            op = input().lower()
            if op == '+':
                self.somar()
            elif op == '-':
                self.subtracao()
            elif op == '-':
                self.subtracao()
            elif op == '/':
                self.divisao()
            elif op == 'c':
                self.resetar()
            elif op == 's':
                break
            else:
                print("Digite um número corretamente, por favor.")

teste = Calculator()
teste.principal()




