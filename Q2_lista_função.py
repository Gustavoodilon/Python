

def cadastrar_livro():

def Emprestimo_de_livros():
    
def Devoluca_do_livro():

def Relatorio_final():


def menu():
    
    while True:
        print("\tMenu gerenciamento estoque")
        print("1 - Cadastro de livros")
        print("2 - Empréstimo de livros")
        print("3 - Devolução de livros")
        print("4 - Relatório final")
        
        escolha = input("\nInforme qual opção deseja consultar: ")
        
        if escolha == '1':
            cadastrar_livro()
        elif escolha == '2':
            Emprestimo_de_livros()
        elif escolha == '3':
            Devoluca_do_livro()
        elif escolha == '4':
            Relatorio_final()



menu()