# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
from cores.colorPrint import color_print

print('-'*60)
print(f"{"Validando entrada de dados em Python":^60}")
print('-'*60)

def leia_int(msg = ''):
    while True:
        try:
            ipt = int(input(msg))
            break
        except (ValueError, TypeError):
            color_print("Erro! Digite um número inteiro válido.", "red")
    return ipt

n = leia_int("Digite um número inteiro: ")
print(f"Você acabou de digitar o número {n}.")