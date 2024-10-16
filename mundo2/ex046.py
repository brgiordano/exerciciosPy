# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep

print("")
for i in range(10, -1, -1):
    print("\r\tCONTAGEM REGRESSIVA: {}{}{}".format("\033[1m", i, "\033[m"), end="")
    sleep(1)
print("\r\t{}FELIZ ANO NOVO!{}".format("\033[4m", "\033[m"))
