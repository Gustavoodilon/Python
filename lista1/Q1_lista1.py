# Crie um programa que verifique se uma palavra ou frase ´e um pal´ındromo, ou seja, se ´e
#lida da mesma maneira de trás para frente.

palavra = input("Informe uma palavra: ")
palindromo = True

for i in range(len(palavra)//2):
    if(palavra[i] != palavra[len(palavra) -i -1]):
        palindromo = False
        break
    
if palindromo:
    print("A palavra é palindrome")
else:
    print("Não é palindrome")