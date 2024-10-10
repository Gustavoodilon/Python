def contar_caracteres(string):
    """Conta a frequência de cada caractere em uma string."""
    frequencia = {}
    
    for caractere in string:
        # Ignora espaços em branco e caracteres não alfanuméricos
        if caractere.isalnum():
            if caractere in frequencia:
                frequencia[caractere] += 1
            else:
                frequencia[caractere] = 1
    
    return frequencia

def mostrar_frequencia(frequencia):
    """Exibe o caractere e o número de vezes que ele aparece na string."""
    for caractere, contagem in frequencia.items():
        print(f"Caractere: '{caractere}' - Frequência: {contagem}")

def main():
    """Função principal para executar o programa."""
    string = input("Digite uma string: ")
    
    frequencia = contar_caracteres(string)
    
    print("Frequência dos caracteres:")
    mostrar_frequencia(frequencia)

# Chama a função principal
main()
