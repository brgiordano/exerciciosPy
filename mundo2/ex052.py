# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
numero = int(input("Digite um número: "))
primo = False

print(f"\tO número {numero} ", end="")
if numero == 1:
    print("NÃO É um número primo, pois só tem um divisor natural.")
else:
    crivoErastotenes = (2, 5, 7)
    for i in crivoErastotenes:
        if numero != i and numero % i == 0:
            print(f"NÃO É um número primo, pois é divisível por {i}.")
            break
        else:
            print("É UM NÚMERO PRIMO!")
            break
