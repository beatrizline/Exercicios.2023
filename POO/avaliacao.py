#TURMA TDS 266
#MIRELLE BEATRIZ DE SOUSA FERREIRA MATRICULA: 2023111MTDS0031
#DIOGO RODRIGUES FEITOSA MATRICULA: 2023111MTDS0033

from datetime import datetime

class Boleto:
    def __init__(self, numero_banco, cod_barra, dt_venc, valor_doc, cedente, devedor):
        data_vencimento_dt = datetime.strptime(dt_venc, "%d/%m/%Y")
        if data_vencimento_dt.weekday() in [7,1]:
            raise ValueError("A data não conta em finais de semana.")
        self.__numero_banco = numero_banco
        self.__codigo_barras = cod_barra
        self.__data_vencimento = dt_venc
        self.__data_pagamento = None
        self.__juros = 0
        self.__multa = 0
        self.__desconto = 0
        self.__valor_documento = valor_doc
        self.__valor_cobrado = 0
        self.__cedente = cedente
        self.__devedor = devedor
        self.__pago = False
        self.__status = "Ativo"

    @property
    def dt_vencimento(self):
        return self.__dt_venc

    @property
    def status(self):
        return self.__status

    @dt_vencimento.setter
    def dt_vencimento(self, conv):
        data_vencimento = datetime.strptime(conv, "%d/%m/%Y")
        if data_vencimento.weekday() in [5,6]:
            raise ValueError("A data não conta em finais de semana.")
        self.__data_vencimento = conv

    def pagar(self, data_pago):
        if self.__pago:
            return

        data_pago = datetime.strptime(data_pago, "%d/%m/%Y")
        dias_atraso = (data_pago - datetime.strptime(self.__data_vencimento, "%d/%m/%Y")).days

        if dias_atraso < 0:
            self.__desconto = 0.05 * self.__valor_documento
            self.__valor_cobrado = self.__valor_documento - self.__desconto
        elif dias_atraso == 0:
            self.__valor_cobrado = self.__valor_documento
        else:
            self.__multa = 0.02 * self.__valor_documento
            self.__juros = 0.005 * dias_atraso * self.__valor_documento
            self.__valor_cobrado = self.__valor_documento + self.__multa + self.__juros

        self.__data_pagamento = data_pago
        self.__pago = True

    def cancelar(self):
        if self.__pago:
            return

        data_atual = datetime.now()
        data_venc = datetime.strptime(self.__data_vencimento, "%d/%m/%Y")

        if data_atual > data_venc:
            print("Não é possível fazer o cancelamento de um boleto vencido.")
            return

        self.__status = 'Cancelado'
        print("Boleto cancelado com sucesso!")

    def __str__(self):
        return f"Numero do Banco: {self.__numero_banco}\nCódigo de Barras: {self.__codigo_barras}\n" \
               f"Data de Vencimento: {self.__data_vencimento}\nData de Pagamento: {self.__data_pagamento}\n" \
               f"Juros: {self.__juros:.2f}\nMulta: {self.__multa:.2f}\nDesconto: {self.__desconto:.2f}\n" \
               f"Prestação paga com sucesso! Valor cobrado: {self.__valor_documento:.2f}\nPrestação paga com sucesso! Valor cobrado: {self.__valor_cobrado:.2f}\n" \
               f"Cedente: {self.__cedente}\nSacado: {self.__devedor}\nPago: {self.__pago}\nStatus: {self.__status}"


print("\nBOLETO\n")

prestacao_da_casa = Boleto('104', '104000629873344', '23/10/2023', 587.54, 'Caixa Economica Federal', 'Francisco Pereira de Sousa')
prestacao_do_carro = Boleto('001', '001348746546497', '26/10/2023', 485.54, 'Banco do Brasil', 'Maria Fernandes da Silva')

prestacao_da_casa.pagar('25/10/2023')
prestacao_do_carro.pagar('25/10/2023')

prestacao_da_casa.pagar('23/10/2023')
prestacao_do_carro.cancelar()

prestacao_colegio = Boleto('026', '02698798786876', '27/10/2023', 265.10, 'Objetivo', 'Pedro de Araujo dos Santos')
prestacao_colegio.cancelar()

prestacao_colegio.pagar('23/10/2023')
print("Boleto não pode mais ser pago pois foi cancelado!")

print(prestacao_da_casa)
print("***************")
print(prestacao_do_carro)
print("***************")
print(prestacao_colegio)
