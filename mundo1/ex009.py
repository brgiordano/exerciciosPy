# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada (de multiplicação).
baseTabuada = int(input("Digite qual a tabuada desejada: "))
print(20*'-')
for i in range(1, 11):
    print(f"|\t{i:>2} x {baseTabuada} = {i*baseTabuada:>2}{" "*4}|")
print(20*'-')