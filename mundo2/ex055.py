# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior: float = 0
menor: float = 0

for i in range(0, 5):
    peso = float(input(f"Digite o peso da {i+1} pessoa (kg): "))
    if i == 0: maior = menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f"\tMaior peso: {maior}kg\n"
      f"\tMenor peso: {menor}kg")