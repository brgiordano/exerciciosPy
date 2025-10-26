# modulo do ex111 e 112
from colors.colorPrint import color_print


def leia_dinheiro(msg = ''):
    valor = ''
    while True:
        try:
            valor = input(msg).replace(',', '.')
            valor = float(valor)
            break
        except ValueError:
            color_print(f"Valor '{valor}' incorreto, digite um valor válido!", "red")
    return valor
