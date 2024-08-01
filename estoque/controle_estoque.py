class ControleEstoque:
    def __init__(self):
        self.produtos = {}
        self.proximo_codigo = 1

    def produto_entrada(self, produto, quantidade):
        if produto.nome in self.produtos:
            self.produtos[produto.nome].quantidade += quantidade
        else:
            produto.codigo = self.proximo_codigo
            self.produtos[produto.nome] = produto
            self.proximo_codigo += 1
        print(f"Entrada de {quantidade} unidades do produto '{produto.nome}' realizada com sucesso.")

    def produto_saida(self, nome_produto, quantidade):
        if nome_produto in self.produtos:
            produto = self.produtos[nome_produto]
            if produto.quantidade >= quantidade:
                produto.quantidade -= quantidade
                print(f"Saída de {quantidade} unidades do produto '{nome_produto}' realizada com sucesso.")
            else:
                print(f"Erro: Quantidade insuficiente de '{nome_produto}' em estoque.")
        else:
            print(f"Erro: Produto '{nome_produto}' não encontrado no estoque.")


    def contagem_produtos(self):
        print("Contagem de Produtos em Estoque:")
        for produto in self.produtos.values():
            print(f"Produto: {produto.nome}, Quantidade: {produto.quantidade}, Valor Unitário: {produto.valor_unit}")


class Produto:
    def __init__(self, nome, quantidade, valor_unit) -> None:
        self.nome = nome 
        self.codigo = None
        self.quantidade = quantidade
        self.valor_unit = valor_unit
        
    
    
    
if __name__ == '__main__':
    controlador = ControleEstoque()
    produto = Produto()
    controlador.produto_entrada(produto)        