# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print("Pares entre 1 e 50:")
for i in range(2, 51, 2):
    print(f"{i:>5}", end="")
    if i % 5 == 0: print()