# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
print('-'*60)
print(f"{"Matriz em python":^60}")
print('-'*60)

matriz = [[],[],[]]
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f"Digite o valor [{i}][{j}]: ")))
print('-'*60)

for l in matriz:
    for c in l:
        print(f"[{c:^5}]", end='')
    print()