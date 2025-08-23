class Produto:
    def __init__(self, nome, preco, quantidade=0):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.vendido = 0  # total vendido

    def entrada(self, qtd):
        self.quantidade += qtd
        print(f"Entrada de {qtd} unidades de {self.nome}. Estoque atual: {self.quantidade}")

    def saida(self, qtd):
        if qtd > self.quantidade:
            print(f"Estoque insuficiente para retirar {qtd} unidades de {self.nome}. Estoque atual: {self.quantidade}")
            return False
        self.quantidade -= qtd
        print(f"Saída de {qtd} unidades de {self.nome}. Estoque atual: {self.quantidade}")
        return True

    def vender(self, qtd):
        if qtd > self.quantidade:
            print(f"Estoque insuficiente para vender {qtd} unidades de {self.nome}. Estoque atual: {self.quantidade}")
            return False
        self.quantidade -= qtd
        self.vendido += qtd
        total = qtd * self.preco
        print(f"Venda de {qtd} unidades de {self.nome}. Total: R$ {total:.2f}. Estoque atual: {self.quantidade}")
        return True

    def __str__(self):
        return f"Produto: {self.nome} | Preço: R$ {self.preco:.2f} | Estoque: {self.quantidade} | Vendido: {self.vendido}"


class Estoque:
    def __init__(self):
        self.produtos = {}

    def cadastrar_produto(self, nome, preco, quantidade=0):
        if nome in self.produtos:
            print(f"Produto {nome} já cadastrado.")
        else:
            self.produtos[nome] = Produto(nome, preco, quantidade)
            print(f"Produto {nome} cadastrado com sucesso.")

    def entrada_produto(self, nome, qtd):
        if nome in self.produtos:
            self.produtos[nome].entrada(qtd)
        else:
            print(f"Produto {nome} não encontrado no estoque.")

    def saida_produto(self, nome, qtd):
        if nome in self.produtos:
            self.produtos[nome].saida(qtd)
        else:
            print(f"Produto {nome} não encontrado no estoque.")

    def vender_produto(self, nome, qtd):
        if nome in self.produtos:
            self.produtos[nome].vender(qtd)
        else:
            print(f"Produto {nome} não encontrado no estoque.")

    def consultar_estoque(self):
        print("\nEstoque atual:")
        for produto in self.produtos.values():
            print(produto)

    def relatorio_vendas(self):
        print("\nRelatório de vendas:")
        total_geral = 0
        for produto in self.produtos.values():
            total_produto = produto.vendido * produto.preco
            print(f"{produto.nome}: {produto.vendido} unidades vendidas - Total: R$ {total_produto:.2f}")
            total_geral += total_produto
        print(f"Total geral das vendas: R$ {total_geral:.2f}")


def menu():
    estoque = Estoque()
    while True:
        print("\n=== Menu ===")
        print("1 - Cadastrar produto")
        print("2 - Entrada de produto")
        print("3 - Saída de produto")
        print("4 - Vender produto")
        print("5 - Consultar estoque")
        print("6 - Relatório de vendas")
        print("0 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço unitário: "))
            qtd = int(input("Quantidade inicial: "))
            estoque.cadastrar_produto(nome, preco, qtd)
        elif escolha == "2":
            nome = input("Nome do produto: ")
            qtd = int(input("Quantidade entrada: "))
            estoque.entrada_produto(nome, qtd)
        elif escolha == "3":
            nome = input("Nome do produto: ")
            qtd = int(input("Quantidade saída: "))
            estoque.saida_produto(nome, qtd)
        elif escolha == "4":
            nome = input("Nome do produto: ")
            qtd = int(input("Quantidade venda: "))
            estoque.vender_produto(nome, qtd)
        elif escolha == "5":
            estoque.consultar_estoque()
        elif escolha == "6":
            estoque.relatorio_vendas()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")


# Para rodar o menu, descomente a linha abaixo:
menu()
