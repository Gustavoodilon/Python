def adicionar_item(lista, item, quantidade):

        if item in lista:
            lista[item.upper()] += quantidade
        else:
            lista[item.upper()] = quantidade
            
def remover_item(lista, item):
    
    if item.upper() in lista:
        del lista[item.upper()]
        print(f"o item '{item}' foi removido")
    else:
        print(f"Não existe nenhum item com este nome: '{lista[item]}'")
        
def mostrar_lista(lista):
    
    if lista:
        print("Lista de itens: ")
        for item, quantidade in lista.items():
            print(f"{item} : {quantidade}")
    else:
        print("A lista esta vazia")

def main():
    lista = {}
    
    while True:
        print()    
        print("1 - adicionar item na lista")    
        print("2 - remover item da lista")    
        print("3 - mostrar lista completa")    
        print("4 - sair")    
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '1':
            item = input("\nInforme o nome do item: ")
            quantidade = int(input(f"Informe a quantiade do item {item}: "))
            adicionar_item(lista, item, quantidade)
        elif opcao == '2':
            item = input("\nInforme o nome do item que deseja remover: ")
            remover_item(lista, item)
        elif opcao == '3':
            print()
            mostrar_lista(lista)
        elif opcao == '4':
            print("\nPrograma encerrado!")
            break
        else:
            print("\Opção invalida, Informe de 1 a 4!")
            
main()