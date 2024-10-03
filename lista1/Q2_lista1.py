def celsius_para_fahrenheit(celsius):
     return [(c * 9/5) + 32 for c in celsius]
    
def fahrenheit_para_celsius(fahrenheit):
    return [(f - 32) * 5/9 for f in fahrenheit]

def exibir_temperaturas(lista, unidade):
    for temp in lista:
        print(f"-------------------------\n{temp:.2f}° {unidade}")
    
def main():
    temperaturas = input("Informe a lista com separação de ',': ")
    temperaturas = [float(t.strip()) for t in temperaturas.split(",")]
    
    escolha = input('1 - Celsius para fahrenehit\n 2 - fahrenehit para celsius: ')
    
    if escolha == '1':
        temperaturas_convertidas = celsius_para_fahrenheit(temperaturas)
        exibir_temperaturas(temperaturas_convertidas, "Fahrenehit")
    elif escolha == '2':
        temperaturas_convertidas = fahrenheit_para_celsius(temperaturas)
        exibir_temperaturas(temperaturas_convertidas, "Celsius")
    else:
        print("Escolha incorreta, informe\n1 - Celsius para fahrenehit\n 2 - fahrenehit para celsius: ")
        
main()