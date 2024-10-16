# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar
# ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime

anoNascimento = int(input("Informe o ano de nascimento: "))
anoAtual = datetime.date.today().year
idade = anoAtual-anoNascimento
anoAlistamento = anoNascimento + 18

print("Em {} você completa {} anos.".format(anoAtual, idade))
if idade < 18:
    print("Seu alistamento deverá ocorrer em {}. Faltam {} anos.".format(anoAlistamento, 18 - idade))
elif idade > 18:
    print("Seu alistamento foi em {}. Passaram {} anos.".format(anoAlistamento, idade - 18))
else:
    print("Seu alistamento deve ocorrer neste ano de {}. Aliste-se!".format(anoAtual))
