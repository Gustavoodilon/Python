alunos = {}

def cadastrar_aluno(nome, nota):
    if nome in alunos:
        print(f"Aluno {nome} ja foi cadastrado")
    else:
        alunos[nome] = nota
        print(f"Aluno {nome} cadastrado com nota {nota}")
        
def mostrar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado")
    else:
        print("Lista de alunos e Notas: ")
        for nome, nota in alunos.items():
            print(f"{nome} : {nota}")
            
def media_turma():
    if not alunos:
        return 0
    media = sum(alunos.values()) / len(alunos)
    return media

def main():
    while True:
        print("\nMenu")
        print("1 - cadastrar aluno")
        print("2 - mostrar alunos")
        print("3 - Calcular media da turma")
        print("4 - sair")
        
        opcao = input("EScolha uma oção: ")
        
        if opcao == '1':
            nome = input("Informe o nome do aluno: ")
            nota = float(input("Informe a nota do aluno: "))
            cadastrar_aluno(nome, nota)
            
        elif opcao == '2':
            mostrar_alunos()
            
        elif opcao == '3':
            media = media_turma()
            print(f"A média da turma é: {media:.2f}")
            
        elif opcao == '4':
            break
        
        else:
            print("Opção invalida. tente novamente")
    
    
main()