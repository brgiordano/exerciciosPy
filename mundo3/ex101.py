# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

print('-'*60)
print(f"{"Funções para votação":^60}")
print('-'*60)
from datetime import date

def voto(nasc: int):
    idade = date.today().year - nasc
    if idade < 16:
        return "NEGADO"
    elif 16 <= idade < 18 or idade >= 70:
        return "OPCIONAL"
    return "OBRIGATÓRIO"

ano_nascimento = int(input("Digite o ano de nascimento: "))
print(f"Com {date.today().year - ano_nascimento} anos o voto é {voto(ano_nascimento)}.")