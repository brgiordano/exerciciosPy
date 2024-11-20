# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
#   a) de 1 até 10, de 1 em 1
#   b) de 10 até 0, de 2 em 2
#   c) uma contagem personalizada
from time import sleep

print('-'*60)
print(f"{"Função de contador":^60}")
print('-'*60)

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio <= fim and passo < 0 or inicio > fim and passo > 0:
        passo *= -1

    if inicio <= fim:
        for c in range(inicio, fim+1, passo):
            print(c, end=' ')
            sleep(0.5)
    else:
        for c in range(inicio, fim-1, passo):
            print(c, end=' ')
            sleep(0.5)
    print("FIM!")


print(f"Contagem de 1 até 10 de 1 em 1:")
contador(1, 10, 1)
print("=-" * 20 +'=')

print(f"Contagem de 10 até 0 de 2 em 2:")
contador(10, 0, 2)
print("=-" * 20 +'=')

print("Personalize a contagem: ")
i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

print("=-" * 20 +'=')
print(f"Contagem de {i} até {f} de {abs(p)} em {abs(p)}:")
contador(i, f, p)
