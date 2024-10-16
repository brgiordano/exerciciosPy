# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
#
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import datetime

print("-=-"*20)
print("Verificador de categoria".center(60))
print("-=-"*20)
anoNascimento = int(input("Digite o ano de nascimento do atleta: "))

anoAtual = datetime.today().year
idade = anoAtual - anoNascimento

print(f"O atleta tem {idade} anos.")

if idade <= 9:
    print("Categoria MIRIM")
elif idade <= 14:
    print("Categoria INFANTL")
elif idade <=  19:
    print("Categoria JUNIOR")
elif idade <= 25:
    print("Categoria SENIOR")
else:
    print("Categoria MASTER")