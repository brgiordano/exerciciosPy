# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
import random
from random import randint

print('-'*60)
print(f"{"Funções para sortear e somar":^60}")
print('-'*60)

def sorteia(lista: list):
    sorteado = random.choices(range(1, 11), k=5)
    lista.extend(sorteado)
    return sorteado

def soma_par(lista: list):
    return sum([v for v in lista if v % 2 == 0])

numeros = []

print(f"Lista atual: {numeros}")
print(f"Soma do valores pares: {soma_par(numeros)}")
print('-'*60)

print(f"Números sorteados: {sorteia(numeros)}")
print(f"Lista atual: {numeros}")
print(f"Soma do valores pares: {soma_par(numeros)}")
print('-'*60)

print(f"Números sorteados: {sorteia(numeros)}")
print(f"Lista atual: {numeros}")
print(f"Soma do valores pares: {soma_par(numeros)}")
print('-'*60)

print(f"Números sorteados: {sorteia(numeros)}")
print(f"Lista atual: {numeros}")
print(f"Soma do valores pares: {soma_par(numeros)}")
print('-'*60)
