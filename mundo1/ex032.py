# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import datetime

ano = int(input("Digite ano - [Digite 0 para o ano atual]: "))
if ano == 0:
    ano = datetime.date.today().year
bissexto: bool

if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
        bissexto = True
else:
        bissexto = False
print("O ano {} {}é um ano bissexto.".format(ano, ""if bissexto else "não "))