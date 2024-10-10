def contador_palavras(frase):
    palavras = frase.split()
    
    freq = {}
    
    for palavra in palavras:
        palavra = palavra.lower() 
        if palavra in freq:
            freq[palavra] += 1
        else:
            freq[palavra] = 1
        
    return freq

def mostrar_frequencia(freq):
    for palavra, contagem in freq.items():
        print(f"Palavra: '{palavra}' - Quantidade repetição: {contagem}")

frase = input("Informe uma frase: ")
print()

frequencia_palavras = contador_palavras(frase)

mostrar_frequencia(frequencia_palavras)
