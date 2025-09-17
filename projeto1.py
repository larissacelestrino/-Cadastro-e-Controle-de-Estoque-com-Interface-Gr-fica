import streamlit as st
from classes import produto, venda, produtos, produtos_salvar, vendas, vendas_salvar, pegar_produto, cliente, busca, clientes, clientes_salvar, pegar_cliente

st.title("Cadastro e controle de estoque ")
produto2 = produtos()
nova_venda = vendas()
clientes1 = clientes()

menu = st.selectbox("Menu", ["Produtos", "Vendas", 'clientes'])

if menu == "Produtos":
    col1, col2 =st.columns(2)
    with col1:
        st.image("pro.jpg")
    with col2:
        st.subheader("Cadastro de produtos")
        nome = st.text_input("Nome do produto")
        preco = st.number_input("Preço", min_value=0.0)
        quantidade = st.number_input("Estoque", min_value=0)        

    if st.button("Salvar Produto"):
        produto2.append(produto(nome, preco, quantidade))
        produtos_salvar(produto2)
        st.balloons()
        st.success(f"Produto '{nome}' cad   astrado com sucesso!")
    if st.button ("mostrar produtos"):
        with open('produtos.txt', 'r') as arquivo:
            conteudo = arquivo.read()  
            st.text(conteudo)          


if menu == "Vendas":
    col1, col2 =st.columns(2)
    with col1:
        st.image("veve.jpg")
    with col2:

        produtos_lista = produtos()
        clientes_lista = clientes()
        st.subheader("registrar venda")
        nomes_produtos = [p.nome for p in produtos_lista]
        nomes_clientes = [c.nome_completo for c in clientes_lista]
        escolha = st.selectbox("Selecione o produto", nomes_produtos)
        escolha1 = st.selectbox("Selecione o cliente", nomes_clientes)
        preco, estoque = pegar_produto(escolha) 
        clientes1 = pegar_cliente(escolha1) 
        quantidade_vend= st.number_input("Quantidade vendida", max_value= estoque)
        data = st.date_input("Informe a data da venda")
    if st.button ("Registrar venda"):
        total = preco * quantidade_vend
        nova_venda=venda(data, escolha, quantidade_vend, total, escolha1)
        vendas_salvar([nova_venda])
        novos_produtos = []
        import os
        temp_path = "produtos1.txt"
        with open(temp_path, "w") as temp:
            for p in produtos_lista:
                if p.nome == escolha:
                    p.quantidade -= quantidade_vend
                temp.write(str(p))
        os.replace(temp_path, "produtos.txt")
        st.success(f"Produto '{escolha}' cadastrado com sucesso!")
        novo_estoque = next((p.quantidade for p in produtos_lista if p.nome == escolha), None)
        produto2 = produtos_lista 
    if st.button ("Mostrar vendas"):
        with open('vendas.txt', 'r') as arquivo:
            conteudo1 = arquivo.read()  
            st.text(conteudo1)   

if menu == "clientes":
    col1, col2 =st.columns(2)
    with col1:
        st.image("clie.png")
    with col2:
        st.subheader("registrar cliente")
        cpf = st.number_input("CPF do cliente", min_value=0, max_value=99999999999)
        nome_completo = st.text_input("Nome completo")
        data_nascimento = st.date_input("Data de nascimento") 
        telefone = st.number_input("Numero do telefone", min_value=0)
        cep = st.number_input("cep", min_value=0) 
    if st.button ("Cadastrar cliente"):
        endereco = busca(cep)
        novo_cliente = cliente(cpf, nome_completo, data_nascimento, endereco, telefone, cep)
        clientes1.append(novo_cliente)
        clientes_salvar(clientes1)
        st.balloons()
    if st.button ("Mostrar clientes"):
        with open('clientes.txt', 'r') as arquivo:
            conteudo2 = arquivo.read()  
            st.text(conteudo2)  

            
