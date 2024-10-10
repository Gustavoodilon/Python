def adicionar_nota(dicionario, aluno, nota):
    """Adiciona a nota de um aluno ao dicionário."""
    dicionario[aluno] = nota

def mostrar_aprovados(dicionario):
    """Exibe os alunos aprovados (nota ≥ 7.0)."""
    aprovados = [aluno for aluno, nota in dicionario.items() if nota >= 7.0]
    if aprovados:
        print("Alunos aprovados:")
        for aluno in aprovados:
            print(aluno)
    else:
        print("Nenhum aluno aprovado.")

def media_turma(dicionario):
    """Retorna a média das notas da turma."""
    if not dicionario:  # Verifica se o dicionário está vazio
        return 0
    total_notas = sum(dicionario.values())
    media = total_notas / len(dicionario)
    return media

def main():
    """Função principal para gerenciar as notas da turma."""
    notas_turma = {}
    
    while True:
        print("\n1 - Adicionar nota")
        print("2 - Mostrar alunos aprovados")
        print("3 - Calcular média da turma")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            aluno = input("Informe o nome do aluno: ")
            nota = float(input(f"Informe a nota do aluno {aluno}: "))
            adicionar_nota(notas_turma, aluno, nota)
            print(f"Nota de {aluno} adicionada.")
        elif opcao == '2':
            mostrar_aprovados(notas_turma)
        elif opcao == '3':
            media = media_turma(notas_turma)
            print(f"Média da turma: {media:.2f}")
        elif opcao == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chama a função principal
main()
