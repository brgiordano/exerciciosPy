# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
#       Exercício 9: Faça um programa que leia um número Inteiro qualquer
#       e mostre na tela a sua tabuada (de multiplicação).
# OBS: JÁ FOI FEITO COM LAÇO FOR NO EX. 09

baseTabuada = int(input("Digite a tabuada de multiplicação desejada: "))
print("\t"+21*'-')
for i in range(1, 11):
    print(f"\t|\t{i:>2} x {baseTabuada:>2} = {i * baseTabuada:>2}\t|")
print("\t"+21*'-')