# Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

soma = 0
somaImpares = 0
contImpar = 0
for i in range (3, 501, 3):
    soma += i
    if i % 2 != 0:
        contImpar += 1
        somaImpares += i
print(f"\nA soma de TODOS os múltiplos de 3 no intervalo entre 1 e 500 é: {soma}")
print(f"A soma dos {contImpar} números ÍMPARES múltiplos de 3 no intervalo entre 1 e 500 é: {somaImpares}")