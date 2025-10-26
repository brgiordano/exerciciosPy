# Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
from colors.colorPrint import color_print

print('-'*60)
print(f"{"Funções aprofundadas em Python":^60}")
print('-'*60)

def leia_int(msg = ''):
    num = ''
    while True:
        try:
            num = input(msg)
            num = int(num)
            break
        except ValueError:
            color_print(f"Erro! Valor '{num}' inválido.", "red")
        except KeyboardInterrupt:
            print("\nEntrada de dados interrompida.")
            return 0
    return num

def leia_float(msg = ''):
    num = ''
    while True:
        try:
            num = input(msg)
            num = float(num)
            break
        except ValueError:
            color_print(f"Erro! Valor '{num}' inválido.", "red")
        except KeyboardInterrupt:
            print("\nEntrada de dados interrompida.")
            return 0
    return num

inteiro = leia_int("Digite um número inteiro: ")
real = leia_float("Digite um número real: ")

print(f"O valor inteiro digitado foi {inteiro} e o real foi {real}")
