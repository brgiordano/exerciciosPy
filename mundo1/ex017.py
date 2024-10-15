# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
import math

catetoOposto = float(input("Digite o cateto oposto: "))
catetoAdjacente = float(input("Digite o cateto adjacente: "))
print(f"A hipotenusa é: {(catetoOposto**2 + catetoAdjacente**2)**(1/2)}")
print(f"A hipotenusa é: {math.hypot(catetoOposto, catetoAdjacente)}")
print(f"A hipotenusa é: {math.sqrt(catetoOposto**2 + catetoAdjacente**2)}")