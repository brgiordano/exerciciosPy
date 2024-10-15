# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random

numero = random.randint(0,5)
palpite = int(input("De 0 a 5, adivinhe o número escolhido: "))
if palpite == numero:
    print("Parabéns, você acertou. O número escolhido foi {}.".format(numero))
else:
    print("Que pena, você errou.")