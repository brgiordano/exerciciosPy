# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import datetime

anoAtual = datetime.today().year
maiores = menores = 0

for i in range (0, 7):
    nascimento = int(input(f"\tDigite o ano de nascimento da {i+1}º pessoa: "))
    idade = anoAtual - nascimento

    if idade < 18:
        menores += 1
    else:
        maiores += 1
print(f"{menores} pessoas ainda não atingiram a maioridade, e {maiores} pessoas são maiores de idade.")