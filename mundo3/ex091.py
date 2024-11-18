# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
print('-'*60)
print(f"{"Jogo de dados":^60}")
print('-'*60)

ranking = {
    "jogador1": randint(1, 6),
    "jogador2": randint(1, 6),
    "jogador3": randint(1, 6),
    "jogador4": randint(1, 6)}

print("Resultados!")
for k, v in ranking.items():
    sleep(0.5)
    print(f"\t{k} tirou {v}.")

print('-'*60)
ranking = dict(sorted(ranking.items(), key=lambda x: x[1], reverse=True))

print(f"\t{"_-_ Ranking _-_":^18}")
for i, k in enumerate(ranking):
    sleep(0.5)
    print(f"{i+1}º lugar: {k} com {ranking[k]}")