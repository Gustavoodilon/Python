#Crie um programa que pe¸ca ao usu´ario uma lista de n´umeros e forne¸ca as seguintes
#estat´ısticas sobre a lista, utilizando fun¸c˜oes:
#• menor_numero(lista): retorna o menor n´umero da lista.
#• maior_numero(lista): retorna o maior n´umero da lista.
#• media(lista): retorna a m´edia dos n´umeros da lista.
#• ocorrencias(lista): retorna um dicion´ario com a frequˆencia de cada n´umero na
#lista.
#Dicas:
#• Use as fun¸c˜oes embutidas min(), max() e sum() para calcular o menor, o maior e a
#m´edia dos n´umeros.
#• Para contar a frequˆencia de cada n´umero, utilize um dicion´ario onde a chave ´e o
#n´umero e o valor ´e o n´umero de ocorrˆencias.

def menor_numero(lista):
    return min(lista)

def maior_numero(lista):
    return max(lista)

def media_lista(lista):
    return sum(lista) / len(lista)

def ocorrencias(lista):
    ocorrencia_dici = {}
    
    for num in lista:
        if num in ocorrencia_dici:
            ocorrencia_dici[num] += 1
        else:
            ocorrencia_dici[num] = 1

    return ocorrencia_dici

def main():
    numeros = input("Digite uma lista de números e separe eles em espaço: ").split()
    numeros = [int(num) for num in numeros]
    
    print("Estátistica da lista")
    print(f"Menor número da lista: {menor_numero(numeros)}")
    print(f"Maior número da lista: {maior_numero(numeros)}")
    print(f"Media da lista: {media_lista(numeros)})")
    
    print()
    print("Ocorrência de cada número: ")
    for numero, ocorrencia in ocorrencias(numeros).items():
        print(f"Número: {numero} - ocorrencias {ocorrencia}")
        
main()    