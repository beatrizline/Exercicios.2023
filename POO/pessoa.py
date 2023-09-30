class Pessoa:
    def __init__(self, nome, idade, peso, altura, sexo, estado='vivo', estado_civil='solteiro', conjuge='none'):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__sexo = sexo
        self.__estado = estado
        self.__estado_civil = estado_civil
        self.__conjuge = conjuge

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, value):
        print('Sem permissão')

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, value):
        print('Sem permissão')

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, value):
        print('Sem permissão')

    @property
    def sexo(self):
        return self.__sexo

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, value):
        print('Sem permissão')

    @property
    def estado_civil(self):
        return self.__estado_civil

    @estado_civil.setter
    def estado_civil(self, value):
        print('Sem permissão')

    @property
    def conjuge(self):
        return self.__conjuge

    @conjuge.setter
    def conjuge(self, value):
        print('Sem permissão')

    def envelhecer(self):
        if self.__estado == 'vivo':
            self.__idade += 1
            if self.__idade < 21:
                self.__altura += 5
                print(f'{self.__nome} está com {self.__idade} anos e {self.altura} cm de altura.')
            else:
                print(f'{self.__nome} não pode mais crescer pois está com {self.__idade} anos ou mais.')
        else:
            print(f'Operação não realizada.{self.nome} está morto(a).')

    def engordar(self):
        if self.__estado == 'vivo':
            self.__peso += 2
        else:
            print(f"Operação não realizada. {self.nome} está morto(a).")

    def emagrecer(self, value):
        if self.__estado == 'vivo':
            self.__peso -= value
        else:
            print(f'Operação não realizada.{self.nome} está morto(a).')

    def crescer(self, value):
        if self.__estado == 'vivo':
            if self.__idade < 21:
                self.__altura += value
                print(f"{self.__nome} cresceu {self.__altura} cm.")
            else:
                print(f"{self.__nome} não pode mais crescer pois está com 21 anos ou mais.")
        else:
            print(f'Operação não realizada.{self.nome} está morto(a).')

    def casar(self, value):
        if self.__estado == 'vivo':
            if self.__estado_civil != 'casado(a)':
                if self.__idade >= 18:
                    #Conjuge
                    if value.__estado == 'vivo':
                        if value.__estado != 'casado(a)':
                            if value.__idade >= 18:
                                if value != self:
                                    self.__estado_civil = 'casado(a)'
                                    value.__estado_civil = 'casado(a)'
                                    self.__conjuge = value
                                    value.__conjuge = self
                                    print(f"{self.__nome} está casado(a) com {value.__nome}.")
                                else:
                                    print('Casamento não permitido. Não pode casar-se consigo mesmo.')
                            else:
                                print(f'Casamento não permitido. {value.__nome} é de menor.')
                        else:
                            print(f'{value.__nome} já está casado(a)')
                    else:
                        print(f'Operação não realizada. {value.__nome} está morto(a).')
                else:
                    print(f'Casamento não permitido. {self.__nome} é de menor.')
            else:
                print(f"Casamento não realizado. {self.__nome} é casado.")
        else:
            print(f"Casamento não realizado. {self.__nome} está morto(a).")

    def morrer(self):
        if self.__estado == 'vivo':
            self.__estado = 'morto'
            print(f"{self.nome} morreu.")
        else:
            print(f"{self.__nome} já está morto(a).")

print('*************')
print("CLASSE PESSOA")
print('*************')

nome1 = Pessoa('Maria',5,20,100,'F')


nome2 = Pessoa('João',5,'20','100','M')


nome3 = Pessoa('Pedro',22,'65','170','M')


nome4 = Pessoa('Bia',18,'55','160','F')


nome5 = Pessoa('Julia',30,'65','170','F')


nome6 = Pessoa('Carlos',2,'11','80','M')


nome7 = Pessoa('Jonas',34,'70','180','M')

print('\nOperações')
print('\n(a)')
nome1.idade = '10'

print('\n(b)')
nome1.envelhecer()

print('\n(c)')
nome3.crescer(2)

print('\n(d)')
nome4.casar(nome6)

print('\n(e)')
nome3.casar(nome1)

print('\n(f)')
nome3.casar(nome5)

print('\n(g)')
nome3.casar(nome4)

print('\n(h)')
nome1.morrer()

print('\n(i)')
nome1.engordar()

print('\n(j)')
nome4.casar(nome7)

print('\n(k)')
nome4.morrer()

print('\n(l)')
nome3.morrer()

print('\n(m)')
nome7.casar(nome5)

print('\n(n)')
nome3.casar(nome4)

print('\n(o)')
nome3.morrer()

print('\n(p)')
nome2.idade = 50