# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

print("-=-"*20)
print(f"{"JOKENPÔ":^60}")
print("-=-"*20)

opcoes = {1: "PEDRA", 2: "PAPEL", 3: "TESOURA"}
print(
    '''OPÇÕES:
    [1] - PEDRA
    [2] - PAPEL
    [3] - TESOURA''')
while True:
    jogadaPlayer = int(input("Escolha a sua jogada: "))
    if 0 < jogadaPlayer <= 3: break
    else:
        print("Jogada inválida!")
        exit(1)
jogadaComputador = randint(1, 3)

sleep(0.5)
print("\n\t\033[1mJO" + " "*5, end="")
sleep(1)
print("KEN" + " " * 5, end="")
sleep(1)
print("PÔ"+"\033[m")
sleep(0.5)

print("\nVocê jogou {} e o computador jogou {}."
      .format(opcoes[jogadaPlayer], opcoes[jogadaComputador]))

sleep(0.5)

if ((jogadaPlayer == 1 and jogadaComputador == 3) or
    (jogadaPlayer == 2 and jogadaComputador == 1) or
    (jogadaPlayer == 3 and jogadaComputador == 2)):
    print("\tVOCÊ VENCEU!")
elif jogadaPlayer == jogadaComputador:
    print("\tEMPATE!")
else:
    print("\tCOMPUTADOR venceu!")