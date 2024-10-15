# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 para viagens mais longas.
distancia = float(input("Digite a distância da viagem (km): "))
preco: float = 0
if distancia > 200:
    preco = distancia * 0.45
else:
    preco = distancia * 0.5
print(f"\tA passagem custará R${preco:.2f}")