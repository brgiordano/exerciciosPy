# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
numero = float(input("Digite um número real: "))
print(f"A parte inteira desse número é: {int(numero)}")
print(f"A parte inteira desse número é: {math.trunc(numero)}")