def calcular_media_ponderada(notas, pesos):
    soma_ponderada = sum(nota * peso for nota, peso in zip(notas, pesos))
    soma_pesos = sum(pesos)
    
    if soma_pesos == 0:
        return 0    
    
    media_ponderada = soma_ponderada / soma_pesos
    return media_ponderada
    
def solicitar_dados():
    notas = []
    pesos = []
    
    while True:
        nota = input("Informe a nota (ou informe 'fim' para encerrar): ")
        if nota.lower() == "fim":
            break
        peso = input("Informe os pesos da prova: ")
        
        notas.append(float(nota))
        pesos.append(float(peso))
        
    return notas, pesos

def main():
    notas, pesos = solicitar_dados()
    
    if len(notas) == 0 or len(notas) != len(pesos):
        print("Tamanho de notas e pesos devem ser iguais")
        
    media = calcular_media_ponderada(notas, pesos)
    print(f"\n\nA media é: {media:.2f}")
    

main()
        