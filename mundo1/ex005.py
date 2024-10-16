# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input("Digite um número inteiro: "))
print("O antecessor do número {0} é: {1}\n"
      "O sucessor do número {0} é: {2}".format(numero, numero-1,numero+1))