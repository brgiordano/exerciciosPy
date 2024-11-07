# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
print('-'*60)
print(f"{"Soma de números":^60}")
print('-'*60)

soma = 0
quantidade = 0
while True:
    numero = int(input("\tDigite um número [999 para finalizar]: "))
    if numero == 999:
        break
    soma += numero
    quantidade += 1
print('-'*60)
print(f"Foram digitados {quantidade} números, e a soma deles é: {soma}.")