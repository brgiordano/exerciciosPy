# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0

for i in range(0, 6):
    numeros = int(input(f"\tDigite o {i+1}º número: "))
    if numeros % 2 == 0:
        soma += numeros
print(f"A soma de todos os valores pares digitados é: {soma}")
