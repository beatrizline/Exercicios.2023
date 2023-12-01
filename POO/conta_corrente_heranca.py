class ContaCorrente:
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self._saldo = saldo

    def creditar(self, valor):
        self._saldo += valor

    def debitar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
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

    def render_juros(self):
        juros = self._saldo * (self.taxa_juros / 100)
        self._saldo += juros

    def __str__(self):
        return f"ContaPoupanca {self.numero} - Saldo: {self._saldo}"


class ContaImposto(ContaCorrente):
    def __init__(self, numero, percentual_imposto, saldo=0):
        super().__init__(numero, saldo)
        self.percentual_imposto = percentual_imposto

    def calcula_imposto(self):
        imposto = self._saldo * (self.percentual_imposto / 100)
        self._saldo -= imposto

    def __str__(self):
        return f"ContaImposto {self.numero} - Saldo: {self._saldo}"


conta_corrente1 = ContaCorrente(numero=1)
conta_corrente2 = ContaCorrente(numero=2)
conta_poupanca1 = ContaPoupanca(numero=3, taxa_juros=2.5)
conta_poupanca2 = ContaPoupanca(numero=4, taxa_juros=2.0)
conta_imposto1 = ContaImposto(numero=5, percentual_imposto=1.5)
conta_imposto2 = ContaImposto(numero=6, percentual_imposto=2.0)

conta_corrente1.creditar(1000)
conta_corrente2.creditar(1500)
conta_poupanca1.creditar(2000)
conta_poupanca2.creditar(2500)

conta_corrente1.transferir(500, conta_corrente2)
conta_poupanca1.render_juros()
conta_imposto1.calcula_imposto()

print(conta_corrente1)
print(conta_corrente2)
print(conta_poupanca1)
print(conta_poupanca2)
print(conta_imposto1)
print(conta_imposto2)
