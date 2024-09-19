from pprint import pprint

aluno = {}
i = 0

while True:
    nome = input(f"\nInforme o nome do aluno{i + 1}: ").title()
    if nome == "Parar":
        break
    aluno[nome] = []
    pprint(aluno)
    i += 1

num_aulas = int(input("\nQuantidade de aulas: "))

for dia in range(num_aulas):
    for nome, lista in aluno.items():
        while True:
            falta = input(f"Dia {dia + 1}: {nome} esta presente? S/N: ").upper()
            if falta == "S":
                lista.append(True)
                break
            if falta == "N":
                lista.append(False)
                break

for nome, lista in aluno.items():
    total = sum(lista)
    p = (total/num_aulas) * 100
    print(f"\n{nome} tem {p:.2f}% de presença")

print()
print()
pprint(aluno)