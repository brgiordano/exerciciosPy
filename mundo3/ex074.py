# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint

print('-'*60)
print(f"{"Números aleatórios em Tupla":^60}")
print('-'*60)
numeros: tuple = ()
qtd_valores = 0

while qtd_valores < 5:
    numero = randint(0,10)
    if numero not in numeros:
        numeros += (numero,)
        qtd_valores += 1

print(f"Os valores sorteados foram: {numeros}")
print(f"O maior valor sorteado foi: {max(numeros)}")
print(f"O menor valor sorteado foi: {min(numeros)}")
