# Aprimore o desafio anterior, mostrando no final:
#   A) A soma de todos os valores pares digitados.
#   B) A soma dos valores da terceira coluna.
#   C) O maior valor da segunda linha.
print('-'*60)
print(f"{"Matriz em python 2":^60}")
print('-'*60)

matriz = [[], [], []]
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f"Digite o valor [{i}][{j}]: ")))
print('-'*60)

print("A matriz digitada foi:")
for l in matriz:
    print('\t', end='')
    for c in l:
        print(f"[{c:^5}]", end='')
    print()

print(f"A soma dos valores pares digitados é: {sum([v for l in matriz for v in l if v % 2 == 0])}.")
print(f"A soma dos valores da terceira coluna é: {sum([l[2] for l in matriz])}.")
print(f"O maior valor da segunda linha é: {max(matriz[1])}.")