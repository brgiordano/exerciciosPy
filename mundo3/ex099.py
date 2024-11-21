# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep

print('-'*60)
print(f"{"Função que descobre o maior":^60}")
print('-'*60)

def maior(*numeros):
    n_max = None
    qtd = 0
    if numeros:
        n_max = max(numeros)
        qtd = len(numeros)
    # retorna uma tupla contendo o maior valor e a quantidade de valores passados
    return n_max, qtd

def print_maior(*valores):
    sleep(0.5)
    print("=-" * 30 + '=')
    resultado = maior(*valores)
    if resultado[0] is not None:
        print("Valores informados:")
        for i, v in enumerate(valores):
            if i==0:
                print(f"\t[{v}", end='')
            else:
                print(f", {v}", end='')
            sleep(0.5)
        print("].")
        # print(f"\t[{", ".join(map(str, valores))}]")
        maior_valor = resultado[0]
        qtd_valores = resultado[1]
        sleep(0.5)
        print(f"{"Foram" if qtd_valores > 1 else "Foi"} "
              f"informado{"s" if qtd_valores > 1 else ''} "
              f"{qtd_valores} valor{"es" if qtd_valores > 1 else ''}, "
              f"e o maior foi {maior_valor}.")
    else:
        sleep(0.5)
        print("Nenhum valor foi informado.")

valores1 = [1,2,3,4,5,6,7,8,9,10]
valores2 = [0, 2]
valores3 = [0]
valores4 = []
valores5 = (2,4,6,8)
valores6 = (11,15,0)
valores7 = (0,)
valores8 = ()
print_maior(10,20,30)
print_maior(0)
print_maior(*valores1, *valores4, *valores8, *valores7)
print_maior(*valores1)
print_maior(*valores2)
print_maior(*valores3)
print_maior(*valores4)
print_maior(*valores5)
print_maior(*valores6)
print_maior(*valores7)
print_maior(*valores8)
print_maior(*valores4, *valores1)
print_maior()
print_maior(*valores1, *valores2, *valores4, *valores8,*valores5)