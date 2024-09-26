estoque = []

def cadastrar_produto():
    print("\n\nCadastro do produto: ")
    nome = str(input( "Informe o nome do Produto: "))
    quantidade = int(input("Informe a quantidade do produto: "))
    preco = float(input("Informe o preço do produto: "))
    
    produto = {
        'nome' : nome,
        'quantidade' : quantidade,
        'preco' : preco
    }
    estoque.append(produto)
    
    print(f"\nProduto '{nome}' cadastrado com sucesso")
    
def remover_produto():
    nome = input("\nInforme o nome do produto que você deseja remover: ")
    
    for produto in estoque:
        if produto['nome'] == nome:
            estoque.remove(produto)
            print(f"\nO produto '{nome}' foi removido com sucesso")
            return
        else:
            print(f"\nProduto {nome} não encontrado")
            
def consultar_produto():
    nome = input("\nInforme o nome do produto que deseja consultar: ")
    
    for produto in estoque:
        if produto['nome'] == nome:
            print(f"\nProduto encontrado {produto}\n")
            return
        else:
            print(f"\nProduto '{nome}' nao encontrado\n")
            
def relatorio_completo_produto():
    if not estoque:
        print("\nNão ha produtos cadastrados")
        return
    else:
        print("\nRelatório completo: ")
        for produto in estoque:
            print(f"Nome: {produto['nome']}\nQuantidade: {produto['quantidade']}\nPreço: R$ {produto['preco']:.2f}\n")
            
def valor_total_estoque():
    for produto in estoque:
        total = sum(produto['quantidade'] * produto['preco'])
    print(f"Valor total em estoque: R$ {total:.2f}")

def menu():
    
    while True:
        print("\tMenu gerenciamento estoque")
        print("1 - Cadastrar produto")
        print("2 - Remover produto")
        print("3 - Consultar produto")
        print("4 - Relatório completo")
        print("5 - Valor total em estoque")
        print("6 - Sair")
    
        escolha = input("\nInforme qual opção deseja consultar: ")
        
        if escolha == '1':
            cadastrar_produto()
        elif escolha == '2':
            remover_produto()
        elif escolha == '3':
            consultar_produto()
        elif escolha == '4':
            relatorio_completo_produto()
        elif escolha == '5':
            valor_total_estoque
        elif escolha == '6':
            break


menu()