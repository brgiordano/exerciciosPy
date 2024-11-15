# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
#   A) Quantas pessoas foram cadastradas.
#   B) Uma listagem com as pessoas mais pesadas.
#   C) Uma listagem com as pessoas mais leves.
from cores.colorPrint import color_print

print('-'*60)
print(f"{"Lista composta e análise de dados":^60}")
print('-'*60)
pessoas = []
while True:
    pessoa = [input('Nome: '), float(input('Peso (kg): '))]
    pessoas.append(pessoa[:])
    while True:
        continuar = input('\tDeseja continuar? [S/N]: ')
        if continuar.upper() not in ['S', 'N']:
            color_print("\tResposta inválida!", "red")
        else: break
    if continuar.upper() == 'N': break
print('-'*60)

print(f"Foram cadastradas {len(pessoas)} pessoas.")
maior_peso = max([p[1] for p in pessoas])
pessoas_maior_peso = [p[0] for p in pessoas if p[1] == maior_peso]
print(f"O maior peso foi de {maior_peso}kg - Peso de: {pessoas_maior_peso}")

menor_peso = min([p[1] for p in pessoas])
pessoas_menor_peso = [p[0] for p in pessoas if p[1] == menor_peso]
print(f"O menor peso foi de {menor_peso}kg - Peso de: {pessoas_menor_peso}")
