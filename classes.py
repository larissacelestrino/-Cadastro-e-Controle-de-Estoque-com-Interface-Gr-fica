class produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade=quantidade
    def __str__(self):
        return f"Produto: {self.nome} || Preco do produto: {self.preco} || Quantidade em estoque: {self.quantidade}\n"
    
class venda:
    def __init__(self, data, produto_vendido, quantidade_estoque, total, cliente1):
        self.data =data
        self.produto_vendido = produto_vendido
        self.quantidade_estoque = quantidade_estoque
        self.total = total
        self.cliente1 = cliente1
    def __str__(self):
        return f"produto vendido: {self.produto_vendido} || quantidade vendida: {self.quantidade_estoque} || data da venda: {self.data} || total da venda: {self.total} || Cliente vinculado: {self.cliente1}\n"


class cliente:
    def __init__ (self, cpf, nome_completo, data_nascimento, endereco, telefone, cep):
        self.cpf = cpf
        self.nome_completo= nome_completo
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.cep = cep
        endereco_dict = busca(cep)
        endereco = f"{endereco_dict.get('street', '')}, {endereco_dict.get('neighborhood', '')}, {endereco_dict.get('city', '')} - {endereco_dict.get('state', '')}"
        self.endereco= endereco
    def __str__ (self) :
        return f" Dados do cliente: CPF: {self.cpf} || Nome completo: {self.nome_completo} || Data de nascimento: {self.data_nascimento} || Telefone: {self.telefone} || CEP: {self.cep} || Endereço: {self.endereco}"    
def busca(cep):
    import requests
    link = f"https://brasilapi.com.br/api/cep/v1/{cep}"
    requisicao = requests.get(link)
    dados = requisicao.json()
    endereco = {
                "state": dados.get("state"),
                "city": dados.get("city"),
                "neighborhood": dados.get("neighborhood"),
                "street": dados.get("street"),
                "service": dados.get("service"),
            }
    return endereco
def clientes():
    clientes_novo = []
    with open("clientes.txt", "r") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split("||")
            cpf = int(partes[0].replace("Dados do cliente: CPF:", "").strip())
            nome = partes[1].replace("Nome completo:", "").strip()
            data = partes[2].replace("Data de nascimento:", "").strip()
            tel = int(partes[3].replace("Telefone:", "").strip())
            cep = int(partes[4].replace("CEP:", "").strip())
            endereco = partes[5].replace("Endereco:", "").strip()
            clientes_novo.append(cliente(cpf, nome, data, tel, cep, endereco ))
        return clientes_novo
def clientes_salvar(clientes):
    with open("clientes.txt", "w") as arquivo:
            for c in clientes:
                arquivo.write(f" Dados do cliente: CPF: {c.cpf} || Nome completo: {c.nome_completo} || Data de nascimento: {c.data_nascimento} || Telefone: {c.telefone} || CEP: {c.cep} || Endereco: {c.endereco}\n")
def pegar_cliente(escolha1):
    clientes1 = []
    with open("clientes.txt", "r") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split("||")
            nome = partes[1].replace("Nome completo:", "").strip()
            if nome == escolha1:
                cpf = int(partes[0].replace("Dados do cliente: CPF:", "").strip())
                data = partes[2].replace("Data de nascimento:", "").strip()
                tel = int(partes[3].replace("Telefone:", "").strip())
                cep = partes[4].replace("CEP:", "").strip()
                endereco = partes[5].replace("Endereco:", "").strip()
                return cliente(cpf, nome, data, tel, cep, endereco)
def produtos():
    nomes = []
    with open("produtos.txt", "r") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split("||")
            nome = partes[0].replace("Produto:", "").strip()
            preco = float(partes[1].replace("Preco do produto:", "").strip())
            quantidade = int(partes[2].replace("Quantidade em estoque:", "").strip())
            nomes.append(produto(nome, preco, quantidade))
        return nomes

def produtos_salvar(produtos):
    with open("produtos.txt", "w") as arquivo:
            for p in produtos:
                arquivo.write(f"Produto: {p.nome} || Preco do produto: {p.preco} || Quantidade em estoque: {p.quantidade}\n")

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
                arquivo.write(f"produto vendido: {v.produto_vendido} || quantidade vendida: {v.quantidade_estoque} || data da venda: {v.data} || total da venda: {v.total} || Cliente vinculado: {v.cliente1} \n")

def pegar_produto(escolha):
    with open("produtos.txt", "r") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split("||")
            nomeproduto = partes[0].replace("Produto:", "").strip()
            if nomeproduto == escolha:
                preco = float(partes[1].replace("Preco do produto:", "").strip())
                estoque = int(partes[2].replace("Quantidade em estoque:", "").strip())
                return preco, estoque