# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

print('-'*60)
print(f"{"Jogo de PAR OU ÍMPAR":^60}")
print('-'*60)
vitorias = 0

while True:
    while True:
        escolha = str(input("PAR ou ÍMPAR [P/I]: ")).strip().upper()
        if escolha not in ['P', 'I']:
            print("Escolha inválida!")
        else: break

    while True:
        numero = input("Escolha um número de 0 a 10: ")
        if not (numero.isdigit() and 0 <= int(numero) <= 10):
            print("Escolha inválida!")
        else:
            numero = int(numero)
            break

    computador = randint(0, 10)
    soma = numero + computador
    print(f"\tVocê: {numero} | Computador: {computador}\n"
          f"\tTotal {soma} = {"PAR" if soma % 2 == 0 else "ÍMPAR"}")

    # venceu = False

    if escolha == 'P':
        if soma % 2 == 0:
            venceu = True
        else:
            venceu = False
    else:
        if soma % 2 != 0:
            venceu = True
        else:
            venceu = False

    if venceu:
        vitorias += 1
        print("\tVocê VENCEU!\n"
              "Vamos jogar novamente!")
        print('-'*60)
    else:
        print("\tVocê PERDEU!")
        print("-"*60)
        break

print(f"Você conseguiu {vitorias} vitória(s)!\n")

