# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
print('-'*60)
print(f"{"Soma de números inteiros":^60}")
print('-'*60)

qtd_digitada = 0
soma = 0

while True:
    valor = int(input("\tDigite um número inteiro [999 para finalizar]: "))
    if valor != 999:
        qtd_digitada += 1
        soma += valor
    else: break

print(f"Foram digitados {qtd_digitada} números, e a soma deles é igual a {soma}")