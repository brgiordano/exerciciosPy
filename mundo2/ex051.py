# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

primeiroTermo = int(input("Digite o primeiro termo de uma PA.: "))
razao = int(input("Digite a razao da PA.: "))

contador = 1
for i in range (0, 10):
    print(f"\t{i+1:0>2}º termo: {primeiroTermo + i * razao:>02}")