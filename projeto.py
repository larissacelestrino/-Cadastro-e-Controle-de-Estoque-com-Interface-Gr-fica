import streamlit as st
estoque=0
precop=0

st.title("Cadastro e Controle de Estoque ")

menu = st.sidebar.radio("Menu", ["Produtos", "Vendas"])

if menu == "Produtos":
    st.subheader("Cadastro de produtos")
    nome = st.text_input("Nome do produto")
    preco = st.number_input("Preço", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade em estoque", min_value=0, step=1)        

    if st.button("Salvar Produto"):
        with open("produtos.txt", "a") as arquivo:
            arquivo.write(f"Produto: {nome} || Preço do produto: {preco} || Quantidade em estoque: {quantidade}\n")
        st.balloons()
        st.success(f"Produto '{nome}' cadastrado com sucesso!")
    if st.button ("mostrar produtos"):
        with open('produtos.txt', 'r') as arquivo:
            conteudo = arquivo.read()  
            st.text(conteudo)          

def nomes ():
    with open("produtos.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            produtos = [linha.split("||")[0].replace("Produto: ", "").strip() for linha in linhas]
            return produtos      
def pegar_produto(escolha):
    with open("produtos.txt", "r") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split("||")
            nomeproduto = partes[0].replace("Produto:", "").strip()
            if nomeproduto == escolha:
                preco = float(partes[1].replace("Preço do produto:", "").strip())
                estoque = int(partes[2].replace("Quantidade em estoque:", "").strip())
                return preco, estoque


if menu == "Vendas":
    st.subheader("registrar venda")
    lista_produtos = nomes()
    if lista_produtos:
        escolha = st.selectbox("Selecione o produto", lista_produtos)
        precop, estoque = pegar_produto(escolha)  
        qtd_vendida = st.number_input("Quantidade vendida", max_value=estoque)
        data = st.date_input("Informe a data da venda")
    if st.button ("registrar venda"):
        total = precop * qtd_vendida
        with open("vendas.txt", "a") as arquivo:
            arquivo.write(f"produto vendido: {escolha} || quantidade vendida: {qtd_vendida} || data da venda: {data} || total da venda: {total}\n")
        with open("produtos.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        linhas_atualizadas = []
        for linha in linhas:
            partes = linha.strip().split("||")
            nome_produto = partes[0].replace("Produto:", "").strip()

        if nome_produto == escolha:
            novo_estoque = estoque - qtd_vendida
            linhas_atualizadas.append(f"Produto: {nome_produto} || Preço do produto: {precop:.2f} || Quantidade em estoque: {novo_estoque}\n")
        st.balloons()
        with open("produtos.txt", "w") as arquivo:
            arquivo.writelines(linhas_atualizadas)
        st.success(f"Produto '{escolha}' cadastrado com sucesso!")
    if st.button ("mostrar vendas"):
        with open('vendas.txt', 'r') as arquivo:
            conteudo1 = arquivo.read()  
            st.text(conteudo1)   

        