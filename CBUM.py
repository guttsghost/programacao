class Produto:
    def __init__(self, nome, desc, preco, tamanho):
        self.nome = nome
        self.desc = desc
        self.preco = preco
        self.tamanho = tamanho

    def Cadastrar(self):
        print("-------CADASTRANDO PRODUTO----------")
        nome = input("Digite o nome do produto: ")
        desc = input("Digite a descrição do produto: ")
        preco = float(input("Digite o preço do produto: "))
        tamanho = input("Digite o tamanho do produto: ")

        print("Nome: {}".format(self.nome))
        print("Descrição: {}".format(self.desc))
        print("Preço: {}".format(self.preco))
        print("Tamanho: {}".format(self.tamanho))

        resp = input("Deseja inserir o produto no estoque: [sim] ou [não]")

        if(resp == 'sim'):
            print("Produto inserido no estoque!")
            print("Produto cadastrado com sucesso!")
        else:
            print("Fim de operação!")



    def cadastrar(self):
        print("Produto cadastrado")

    def Autenticar(self):
        print("Autenticado")

    def Atualizar(self):
        print("Produto Atualizado")
    
    def Deletar(self):
        print("Produto deletado")

p1 = Produto("Pincel", ' Cor Vermelho' , 7.00 , " não especificado")
print(p1.nome)
print(p1.desc)
print(p1.preco)
print(p1.tamanho)
print("---------------------------------")
p1.cadastrar()
p1.Autenticar()
p1.Atualizar()
p1.Deletar()