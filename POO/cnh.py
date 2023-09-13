# Utilizando o processo de abstraçao, implemente uma classe em python que represente uma carteira de habilitaçao.
# Identifique mutaveis e imutaveis, implemente um construtor da classe e metodos para manipulaçao dos atributos mutaveis.
# Faça todas as validaçoes possiveis. Crie objetos para testar os metodos implementados;

import datetime

class Cnh:
    def __init__(self, nome, ident, cpf, data):
        self.nome = nome
        self.ident = ident
        self.cpf = cpf
        self.data = data

    def nomear(self):
        print(f"NOME: {self.nome}")


    def validar_rg(self):
        if len(self.ident) == 7:
            print(f'DOC.IDENTIDADE / ÓRG.EMISSOR/UF: {self.ident}')
        else:
            print("ERRO! DIGITE UM NÚMERO DE RG VÁLIDO")


    def validar_cpf(self):
        if len(self.cpf) == 11:
            print(f'CPF: {self.cpf}')
        else:
            print("ERRO! DIGITE SEU NÚMERO DE CPF: ")


    def validar_data(self):
        n = self.data.split("/")
        dia, mes, ano = n
        ano = int(ano)
        validade = int(ano + 5)

        print(f"A DATA DA SUA HABILITAÇÃO É: {dia}/{mes}/{ano}")
        print(f"A DATA DE VALIDADE DA SUA HABILITAÇÃO É: {dia}/{mes}/{validade}")

        agora = datetime.datetime.now()
        dia1 = agora.day
        mes2 = agora.month
        ano3 = agora.year

        if validade < int(ano3):
            print("CNH EXPIROU. RENOVE IMEDIATAMENTE")
        else:
            print("CNH VÁLIDA. PARABÉNS!")


resposta1 = Cnh(input("DIGITE SEU NOME COMPLETO: "), input("DIGITE SEU NÚMERO DE RG: "),input("DIGITE SEU CPF COMPLETO: " ), input("DIGITE A DATA DE EMISSÃO DA SUA CNH: "))


print("\nVÁLIDA EM TODO TERRITÓRIO NACIONAL BRASILEIRO - CNH")
resposta1.nomear()
resposta1.validar_rg()
resposta1.validar_data()
