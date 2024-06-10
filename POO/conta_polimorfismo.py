# Reescreva as classes referentes ao exercício de Herança com a seguinte modificação: 
# Na classe ContaCorrente, acrescente um método sacar(self,valor). Este método debita o valor que foi passado no argumento do saldo da conta e cobra R$ 2,00 por cada saque efetuado. Ex: conta.sacar(20) vai debitar R$ 22,00 da conta. 
# Na classe ContaPoupança que é filha de ContaCorrente, reescreva o método sacar(self,valor). Este método cobra R$ 0,50 para cada saque efetuado a partir do 5º saque. Ou seja, Toda instancia de ContaPoupanca pode efetuar 4 saques sem cobrança de tarifa. A partir do 5º saque, é debitado o valor do saque mais R$ 0,50. 
# Escreva uma classe Banco que faz uma associação 1:N com ContaCorrente. Nesta classe, crie um método polimórfico adicionar_conta, que é responsável por adicionar uma instancia de ContaCorrente ou ContaPoupança na lista de contas desta classe.
# Crie um outro método polimórfico Sacar(self,conta). Este método vai chamar o método sacar respectivo do objeto que foi passado no argumento. 
# Na execução, crie objetos para representar contas e banco e  teste os métodos polimórficos.


class ContaCorrente:
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self._saldo = saldo

    def creditar(self, valor):
        self._saldo += valor

    def debitar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor + 2 
        else:
            print("Saldo insuficiente.")

    def transferir(self, valor, conta_destino):
        if valor <= self._saldo:
            self._saldo -= valor
            conta_destino.creditar(valor)
        else:
            print("Saldo insuficiente para transferência.")

    @property
    def saldo(self):
        return self._saldo

    def __str__(self):
        return f"ContaCorrente {self.numero} - Saldo: {self._saldo}"


class ContaPoupanca(ContaCorrente):
    def __init__(self, numero, taxa_juros, saldo=0):
        super().__init__(numero, saldo)
        self.taxa_juros = taxa_juros
        self.saques = 0  

    def sacar(self, valor):
        self.saques += 1
        if self.saques > 4:
            valor += 0.50   
        super().debitar(valor)

    def render_juros(self):
        juros = self._saldo * (self.taxa_juros / 100)
        self._saldo += juros

    def __str__(self):
        return f"ContaPoupanca {self.numero} - Saldo: {self._saldo}"


class Banco:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def sacar(self, conta):
        conta.sacar(50)



banco = Banco()
conta_corrente1 = ContaCorrente(numero=1)
conta_poupanca1 = ContaPoupanca(numero=2, taxa_juros=2.0)
banco.adicionar_conta(conta_corrente1)
banco.adicionar_conta(conta_poupanca1)
banco.sacar(conta_corrente1)
banco.sacar(conta_poupanca1)

print(conta_corrente1)
print(conta_poupanca1)
