# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
# DESAFIO 28:
        # Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
        # # e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
        # # O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint

# melhorando para quente e morno e 0 e 100

numero = randint(0, 100)
palpite = int(input("De 0 a 100, adivinhe o número escolhido: "))
dicionario_precisao = {'q': "QUENTE", 'm': "MORNO", 'f': "FRIO"}
tentativas = 1
resultado_precisao = None
precisao = None

while palpite != numero:
    precisao = abs(numero - palpite)
    match precisao:
        case p if p >= 30:
            resultado_precisao = 'f'
        case p if 11 <= p < 30:
            resultado_precisao = 'm'
        case p if p < 11:
            resultado_precisao = 'q'

    palpite = int(input("[você está {:^6}] tente um número {}: ".format
                        (dicionario_precisao[resultado_precisao],
                         "MAIOR" if numero > palpite else "MENOR")))
    tentativas += 1
if tentativas == 1:
    print(f"Parabéns, você acertou de PRIMEIRA! O número escolhido foi {numero}")
else:
    print(f"Parabéns, você acertou com {tentativas} tentativas! O número escolhido foi {numero}.")

