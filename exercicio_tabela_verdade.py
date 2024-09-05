print("|a\t|b\t|a * b\t|")

for a in [False, True]:
    for b in [False, True]:
        print(f"|{a}\t|{b}\t|{a and b}\t|")
        
print("\n|a\t|b\t|a + b\t|")
for a in [False, True]:
    for b in [False, True]:
        print(f"|{a}\t|{b}\t|{a or b}\t|")

print("\n|a\t|b\t|a ^ b\t|")
for a in [False, True]:
    for b in [False, True]:
        print(f"|{a}\t|{b}\t|{a ^ b}\t|")
        
print()
print()

a = 0b1010  # 10 em decimal
b = 0b1100  # 12 em decimal

print(a & b)  # 0b1000

print(a | b)  # 0b1110

print(a ^ b)  # 0b0110

print()
print()

lista = [True, False, True]

print(any(lista)) #any quantdo qualquer elemento for True, ele retorna True
print(not any(lista)) #not any inverte o retorno
print(all(lista)) 
print(not all(lista)) 
