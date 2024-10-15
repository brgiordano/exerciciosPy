# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math

numero = int(input("Digite um número: "))
print("\tO dobro de {0} é: {1}\n"
      "\tO triplo de {0} é: {2}\n"
      "\tA raiz quadrada de {0} é: {3:.2f}".format(numero, numero*2, numero*3, math.sqrt(numero)))