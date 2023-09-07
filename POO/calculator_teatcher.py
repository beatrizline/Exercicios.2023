class Calculadora:
  estado = 'desligado'
  numero1 = None
  numero2 = None
  operação = None
  resultado = None

  def ligar(self):
    self.estado = 'ligado'
    self.resetar()
    self.calcular_expressões()

  def tem_numeros(self,string):
    #Verifica se a string informada possui um número.
    return any(char.isdigit() for char in string)

  def calcular_expressões(self):
    while True:
      print(f'Digitar Número\t (+) - somar\t (-)-subtrair\t (*)-multiplicar (/)-dividir (C)-resetar')
      #print(f'numero1:{self.numero1} numero2:{self.numero2} oper:{self.operação}')
      op=(input())

      if self.tem_numeros(op):
        if self.numero1 ==None and self.operação==None:
           self.numero1 = float(op)
        else:
          self.numero2 = float(op)
      elif op=='+':
          self.operação = '+'
      elif op=='-':
          self.operação = '-'
      elif op=='C':
          self.resetar()

      self.mostra_resultado()


  def mostra_resultado(self):
    if self.numero1!=None and self.numero2!=None and self.operação!=None:
      if self.operação == '+':
            self.resultado = self.somar(self.numero1,self.numero2)
            print(f'{self.numero1}+{self.numero2}={self.resultado}')
      elif self.operação=='-':
            self.resultado = self.diminuir(self.numero1,self.numero2)
            print(f'{self.numero1}-{self.numero2}={self.resultado}')

      self.numero1=self.resultado
      self.numero2=None
      self.operação=None

  def desligar(self):
    self.estado = 'desligado'

  def resetar(self):
    self.numero1 = None
    self.numero2 = None
    self.operação = None
    self.resultado = None
    print(self.resultado)

  def somar(self,n1,n2):
    return n1+n2

  def diminuir(self,n1,n2):
    return n1-n2


