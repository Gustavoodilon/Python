from pprint import pprint

aluno = {}
i = 0

while True:
    nome = input(f"Informe o nome do aluno {i + 1}: ").title()
    if nome == "Parar":
        break
    aluno[nome] = []
    pprint(aluno)
    i += 1

num_avaliacoes = int(input("Informe a quantidade de avaliações: "))

for avaliacao in range(num_avaliacoes):
    for nome, lista in aluno.items():
        while True:
            notas = float(input(f"Informe a nota da avaliação {avaliacao + 1} do {nome}: ")).upper()
            
            if notas < 10 or notas > 0:
                lista.append(notas)
                break
    

for nome, lista in aluno.items():
    total = sum(lista)
    media = (total/num_avaliacoes)
    print(f"\nA media do {nome} é {media}") 
