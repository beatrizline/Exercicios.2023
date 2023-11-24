#Codifique em python a associação de classes abaixo:
#Obs:
#a) fazer as críticas para não adicionar um arquivo maior que o espaço disponível no
#PenDrive
#b) Não permitir a adição de arquivos com mesmo nome
#c) No método __str__(), listar todos os arquivos do penDrive com seus respectivos
#tamanhos, colocar o total ocupado (em MB) e o total livre em (MB)

# Class PenDrive e class Arquivo. Arquivo precisa de PenDrive para existir e não podendo existir se Pendrive também não existir.
# Pen Drive recebe os atributos: ID e Capacidade e os métodos: Formatar(), Adicionar(),Apagar(),Copiar_para_outro_pendrive(), Mover_para_outro_pendrive()
# Arquivo recebe os atributos: Nome, Tipo, Tamanho(MB) e o método: Renomear()

class PenDrive:
    def __init__(self, id, capacidade):
        self.id = id
        self.capacidade = capacidade
        self.arquivos = []

    def formatar(self):
        self.arquivos = []

    def adicionar(self, arquivo):
        if self.espaco_livre() >= arquivo.tamanho:
            if not self.arquivo_existente(arquivo.nome):
                self.arquivos.append(arquivo)
                print(f"Arquivo {arquivo.nome} adicionado ao PenDrive.")
            else:
                print(f"Erro: Já existe um arquivo com o nome {arquivo.nome}.")
        else:
            print("Erro: Espaço insuficiente no PenDrive.")

    def apagar(self, nome_arquivo):
        for arquivo in self.arquivos:
            if arquivo.nome == nome_arquivo:
                self.arquivos.remove(arquivo)
                print(f"Arquivo {nome_arquivo} removido do PenDrive.")
                return
        print(f"Erro: Arquivo {nome_arquivo} não encontrado.")

    def copiar_para_outro_pendrive(self, arquivo, outro_pendrive):
        if self.arquivo_existente(arquivo.nome):
            if outro_pendrive.espaco_livre() >= arquivo.tamanho:
                outro_pendrive.adicionar(arquivo)
                print(f"Arquivo {arquivo.nome} copiado para outro PenDrive.")
            else:
                print("Erro: Espaço insuficiente no PenDrive de destino.")
        else:
            print(f"Erro: Arquivo {arquivo.nome} não encontrado no PenDrive de origem.")

    def mover_para_outro_pendrive(self, arquivo, outro_pendrive):
        if self.arquivo_existente(arquivo.nome):
            if outro_pendrive.espaco_livre() >= arquivo.tamanho:
                outro_pendrive.adicionar(arquivo)
                self.apagar(arquivo.nome)
                print(f"Arquivo {arquivo.nome} movido para outro PenDrive.")
            else:
                print("Erro: Espaço insuficiente no PenDrive de destino.")
        else:
            print(f"Erro: Arquivo {arquivo.nome} não encontrado no PenDrive de origem.")

    def espaco_livre(self):
        ocupado = sum(arquivo.tamanho for arquivo in self.arquivos)
        return self.capacidade - ocupado

    def arquivo_existente(self, nome_arquivo):
        return any(arquivo.nome == nome_arquivo for arquivo in self.arquivos)

    def __str__(self):
        resultado = f"Conteúdo do PenDrive {self.id}:\n"
        for arquivo in self.arquivos:
            resultado += f"{arquivo.nome} ({arquivo.tamanho} MB)\n"
        total_ocupado = sum(arquivo.tamanho for arquivo in self.arquivos)
        total_livre = self.capacidade - total_ocupado
        resultado += f"Total Ocupado: {total_ocupado} MB\n"
        resultado += f"Total Livre: {total_livre} MB"
        return resultado


class Arquivo:
    def __init__(self, nome, tipo, tamanho):
        self.nome = nome
        self.tipo = tipo
        self.tamanho = tamanho

    def renomear(self, novo_nome):
        self.nome = novo_nome
        print(f"Arquivo renomeado para {novo_nome}.")

print('\n*********************')
pendrive1 = PenDrive(id=1, capacidade=1000)
arquivo1 = Arquivo(nome="documento.txt", tipo="txt", tamanho=50)
arquivo2 = Arquivo(nome="foto.jpg", tipo="jpg", tamanho=200)


pendrive1.adicionar(arquivo1)
pendrive1.adicionar(arquivo2)


print(pendrive1)


pendrive2 = PenDrive(id=2, capacidade=500)


pendrive1.copiar_para_outro_pendrive(arquivo1, pendrive2)


pendrive1.mover_para_outro_pendrive(arquivo2, pendrive2)


print(pendrive1)
print(pendrive2)
