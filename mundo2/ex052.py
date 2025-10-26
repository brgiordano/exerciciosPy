# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = 0
while True:
    try:
        numero = int(input("Digite um número: "))
        if numero < 0: numero *= -1
        break
    except ValueError:
        continue

primo = False
divisores = [1]

print(f"\tO número {numero} ", end="")
if numero == 1:
    print(f"NÃO É um número primo, pois só tem um divisor natural.")
else:
    for i in range(2, numero//2+1):
        if numero % i == 0:
            divisores.append(i)

    divisores.append(numero)

    if len(divisores) > 2 or numero == 0:
        print(f"NÃO É um número primo.")
    else:
        print("É UM NÚMERO PRIMO!")

if numero != 0:
    print("Divisores:", divisores)
    print("Total de divisores:", len(divisores))
