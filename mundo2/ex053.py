# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,desconsiderando os espaços.
# Exemplos de palíndromos:
#   APOS A SOPA,
#   A SACADA DA CASA,
#   A TORRE DA DERROTA,
#   O LOBO AMA O BOLO,
#   ANOTARAM A DATA DA MARATONA.

print("-=-" * 20)
print(f"|{"IDENTIFICADOR DE PALÍNDROMOS":^58}|")
print("-=-" * 20)

frase = str(input("Digite uma frase: "))
verifica = frase.replace(" ", "").strip().upper()

print(f"A frase '{frase}'", end=" ")

for i in range(0, len(verifica) // 2):
    if verifica[i] != verifica[(len(verifica) - 1) - i]:
        print("NÃO É um palíndromo.".format(frase))
        break
    else:
        print("É UM PALÍNDROMO.".format(frase))
        break
