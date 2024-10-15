# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar
# ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime

anoNascimento = int(input("Informe o ano de nascimento: "))
anoAtual = datetime.date.today().year
idade = anoAtual-anoNascimento

if idade < 18:
    print("Você ainda deve se alistar")
