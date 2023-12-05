#DUPLA: MIRELLE BEATRIZ DE SOUSA FERREIRA 2023111MTDS0031 E THIAGO LIMA CRUZ 2022211MTDS0026

class Produto:
    def __init__(self, id, descricao, valor):
        self.__id = id
        self.__descricao = descricao
        self.__valor = valor
    
    @property
    def id(self):
        return self.__id
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def valor(self):
        return self.__valor
    
    def __str__(self):
        return f"ID: {self.__id}, Descrição: {self.__descricao}, Valor: {self.__valor}"


class Itens_Compra:
    def __init__(self, id, produto, quantidade, valor):
        self.__id = id
        self.__produto = produto
        self.__quantidade = quantidade
        self.__valor = valor
    
    @property
    def id(self):
        return self.__id
    
    @property
    def produto(self):
        return self.__produto
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @property
    def valor(self):
        return self.__valor


class Compra:
    def __init__(self, nota_fiscal, data, cpf_cliente):
        self.__nota_fiscal = nota_fiscal
        self.__data = data
        self.__cpf_cliente = cpf_cliente
        self.__itens = []
        self.__valor_original = 0
    
    @property
    def nota_fiscal(self):
        return self.__nota_fiscal
    
    @property
    def data(self):
        return self.__data
    
    @property
    def cpf_cliente(self):
        return self.__cpf_cliente
    
    @property
    def itens(self):
        return self.__itens
    
    @property
    def valor_original(self):
        return self.__valor_original
    
    def adiciona_itens(self, itens_compra):
        self.__itens.append(itens_compra)
        self.__valor_original += itens_compra.valor
    
    def calcula_valor_final(self):
        return self.__valor_original
    
    def __str__(self):
        itens_str = "\n".join([f"  {item.produto.nome} - Quantidade: {item.quantidade} - Valor: {item.valor}" for item in self.__itens])
        return f"Nota Fiscal: {self.__nota_fiscal}\nData: {self.__data}\nCPF Cliente: {self.__cpf_cliente}\nItens:{itens_str}\nValor Original: {self.__valor_original}"


class A_vista(Compra):
    def __init__(self, nota_fiscal, data, cpf_cliente, perc_desconto):
        super().__init__(nota_fiscal, data, cpf_cliente)
        self.__perc_desconto = perc_desconto
    
    def calcula_valor_final(self):
        valor_com_desconto = super().calcula_valor_final() * (1 - self.__perc_desconto / 100)
        return valor_com_desconto
    
    def __str__(self):
        return f"{super().__str__()}, Desconto: {self.__perc_desconto}%"


class A_prazo(Compra):
    def __init__(self, nota_fiscal, data, cpf_cliente, num_parcelas):
        super().__init__(nota_fiscal, data, cpf_cliente)
        self.__num_parcelas = num_parcelas
    
    def calcula_valor_final(self):
        num_parcelas = self.__num_parcelas
        if num_parcelas == 1:
            return super().calcula_valor_final()
        elif 2 <= num_parcelas <= 5:
            return super().calcula_valor_final() * 1.10
        elif 6 <= num_parcelas <= 10:
            return super().calcula_valor_final() * 1.15
        else:
            raise ValueError("Número de parcelas inválido. Deve estar entre 1 e 10.")
    
    def calcula_valor_parcela(self):
        return self.calcula_valor_final() / self.__num_parcelas
    
    def __str__(self):
        return f"{super().__str__()}, Parcelas: {self.__num_parcelas}"

class Loja:
    def __init__(self, nome_loja):
        self.__nome_loja = nome_loja
        self.__compras = []
    
    def adiciona_compra(self, compra):
        self.__compras.append(compra)
    
    def imprime_compras(self):
        for compra in self.__compras:
            print(compra)
    
    def __str__(self):
        compras_str = "\n".join([f"{compra}" for compra in self.__compras])
        return f"Loja: {self.__nome_loja}\nCompras:\n{compras_str}"
        

