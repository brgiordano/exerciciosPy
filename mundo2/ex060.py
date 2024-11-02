# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input("Dígite um número inteiro não negativo: "))
while numero < 0:
    numero = int(input("Valor inválido, digite um valor inteiro não negativo: "))

valor_atual = numero
fatorial = 1
while valor_atual > 0:
    fatorial *= valor_atual
    valor_atual -= 1

print(f"O fatorial de {numero} ({numero}!) = {fatorial}.")
