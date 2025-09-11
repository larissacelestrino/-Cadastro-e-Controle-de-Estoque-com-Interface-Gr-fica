class produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade=quantidade
    def __str__(self):
        return f"Produto: {self.nome} || Preço do produto: {self.preco} || Quantidade em estoque: {self.quantidade}\n"
    
class venda:
    def __init__(self, data, produto_vendido, quantidade_estoque, total):
        self.data =data
        self.produto_vendido = produto_vendido
        self.quantidade_estoque = quantidade_estoque
        self.total = total
    def __str__(self):
        return f"produto vendido: {self.produto_vendido} || quantidade vendida: {self.quantidade_estoque} || data da venda: {self.data} || total da venda: {self.total}\n"

def produtos():
    nomes = []
    with open("produtos.txt", "r") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split("||")
            nome = partes[0].replace("Produto:", "").strip()
            preco = float(partes[1].replace("Preço do produto:", "").strip())
            quantidade = int(partes[2].replace("Quantidade em estoque:", "").strip())
            nomes.append(produto(nome, preco, quantidade))
        return nomes

def produtos_salvar(produtos):
    with open("produtos.txt", "w") as arquivo:
            for p in produtos:
                arquivo.write(f"Produto: {p.nome} || Preço do produto: {p.preco} || Quantidade em estoque: {p.quantidade}\n")

def vendas():
    vendidos = []
    with open("vendas.txt", "r") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split("||")
            data = partes[2].replace("data da venda:", "").strip()
            produto_vendido = partes[0].replace("produto vendido:", "").strip()
            quantidade_estoque = int(partes[1].replace("quantidade vendida:", "").strip())
            total = float(partes[3].replace("total da venda:", "").strip())
            vendidos.append({"data": data, "produto": produto_vendido,"quantidade": quantidade_estoque, "total": total})
        return vendidos
            
def vendas_salvar(vendas):
    with open("vendas.txt", "a") as arquivo:
            for v in vendas:
                arquivo.write(f"produto vendido: {v.produto_vendido} || quantidade vendida: {v.quantidade_estoque} || data da venda: {v.data} || total da venda: {v.total}\n")

def pegar_produto(escolha):
    with open("produtos.txt", "r") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split("||")
            nomeproduto = partes[0].replace("Produto:", "").strip()
            if nomeproduto == escolha:
                preco = float(partes[1].replace("Preço do produto:", "").strip())
                estoque = int(partes[2].replace("Quantidade em estoque:", "").strip())
                return preco, estoque