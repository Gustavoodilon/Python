#Crie duas listas: nomes e notas. Use input() para adicionar pelo menos 3 alunos.

nomes = []
notas = []

for i in range(3):
    nome = (input(f"Informe o nome do {i + 1}° aluno: "))
    nomes.append(nome)
    nota = int(input(f"Informe nota do {i + 1}° aluno: "))
    notas.append(nota)

status = []

for nota in notas:
    if nota >= 7:
        resultado = "Aprovado"
        
    elif nota < 7 and nota >=3:
        resultado = "Recuperação"
        
    else:
        resultado = "Reprovado"
    
    status.append(resultado)


print()
print()
for i in range(3):   
      
    print(f"Nome: {nomes[i]}, situação: {status[i]}")
    
aprovados = all(stat == "Aprovado" for stat in status)
recuperação = any(stat == "Recuperação" for stat in status)

print("\nResumo da Turma:")
if aprovados: P = ("Sim")
else: P = ("Não")

if recuperação:
    R = ("Sim")
else: R = ("Não")

print(f"Todos estão aprovados? {P}")
print(f"Há pelo menos um aluno em recuperação? {R}")

        
