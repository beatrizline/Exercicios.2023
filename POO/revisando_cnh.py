
# Utilizando o processo de abstração, implemente uma classe em python que represente uma
# carteira de habilitação. Identifique atributos mutáveis e imutáveis, implemente um construtor
# da classe e métodos para manipulação dos atributos mutáveis. Faça todas as validações
# possíveis. Crie objetos para testar os métodos implementados.

import datetime

class Cnh:
    def __init__(self, nome, identid, cpf, data, data_nasc, filiacao, cat_ab=None, obs='Sem Observações'):
        self.nome = nome
        self.identid = identid
        self.cpf = cpf
        self.data = data
        self.data_nasc = data_nasc
        self.filiacao = filiacao
        self.cat_ab = cat_ab
        self.obs = obs

    def nomear(self):
        print(f"NOME: {self.nome}")

    def validar_rg(self, rg):
        rg = self.identid
        return any(char.isdigit() for char in rg)

    def validar_cpf(self, cpf):
        cpf = self.cpf
        return any(char.isdigit() for char in cpf)

    def ver_rg(self):
        self.validar_rg(self.identid)
        if len(self.identid) == 7:
            print(f'DOC.IDENTIDADE / ÓRG.EMISSOR/UF: {self.identid}')
        else:
            print("ERRO! DIGITE UM NÚMERO DE RG VÁLIDO")

    def ver_cpf(self):
        self.validar_cpf(self.cpf)
        if len(self.cpf) == 11:
            print(f'CPF: {self.cpf}')
        else:
            print("ERRO! DIGITE SEU CPF CORRETAMENTE")

    def validar_data(self):
        n = self.data.split("/")
        dia, mes, ano = n
        ano = int(ano)
        validade = int(ano) + 5

        print(f"A DATA DA SUA HABILITAÇÃO É: {dia}/{mes}/{ano}")
        print(f"A DATA DE VALIDADE DA SUA HABILITAÇÃO É: {dia}/{mes}/{validade}")

        agora = datetime.datetime.now()
        ano = agora.year

        if validade < int(ano):
            print("---------CNH EXPIROU. RENOVE IMEDIATAMENTE---------")
        else:
            print("---------CNH VÁLIDA. PARABÉNS!---------")

    def data_nascimento(self):
        print(f'DATA NASCIMENTO(dd/mm/aaaa): {self.data_nasc}')

    def ver_filiacao(self):
        print(f'FILIAÇÃO(SOMENTE O NOME COMPLETO DE UM RESPONSÁVEL): {self.filiacao}')

    def categoria(self):
        print("QUAL TIPO É A SUA CATEGORIA?")
        escolha = input('A, B ou AB: ').upper()
        self.cat_ab = escolha
        print(f'TIPO CATEGORIA: {self.cat_ab}')

    def observacao(self):
        print(self.obs)


resposta1 = Cnh(input("DIGITE SEU NOME COMPLETO: "), input("DIGITE SEU NÚMERO DE RG: "), input("DIGITE SEU CPF COMPLETO: " ), input("DIGITE A DATA DE EMISSÃO DA SUA CNH: "), input("DIGITE SUA DATA DE NASCIMENTO: "), input("DIGITE SUA FILIAÇÃO(SOMENTE O NOME COMPLETO DE UM RESPONSÁVEL): "))

print("\nVÁLIDA EM TODO TERRITÓRIO NACIONAL BRASILEIRO - CNH")
resposta1.nomear()
resposta1.ver_rg()
resposta1.ver_cpf()
resposta1.validar_data()
resposta1.data_nascimento()
resposta1.ver_filiacao()
resposta1.categoria()
resposta1.observacao()