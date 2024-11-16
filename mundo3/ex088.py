# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from random import sample
from time import sleep

print('-'*60)
print(f"{"Palpites para a mega sena":^60}")
print('-'*60)

qtd_jogos = int(input("Quantos jogos deseja sortear: "))
jogos = []
for i in range(qtd_jogos):
    jogo = sorted(sample(range(1,61), 6))
    jogos.append(jogo)

print('-'*60)
print("Sorteando jogos:")
for i, jogo in enumerate(jogos):
    numeros = ", ".join(f"{n:02}" for n in jogo)
    print(f"\tJogo {i+1:02}: [{numeros}]")
    sleep(0.4)
print(f"{qtd_jogos} jogo(s) sorteado(s).")