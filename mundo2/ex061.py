# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
# DESAFIO 51:
#       # Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#       # No final, mostre os 10 primeiros termos dessa progressão.

print('-'*30)
print(f"{"Progressão Aritmética":^30}")
print('-'*30)

primeiroTermo = int(input("Digite o primeiro termo da P.A: "))
termoN = primeiroTermo
razao = int(input("Digite a razão da P.A: "))
qtdTermos = 1
print("Os 10 primeiros termos da P.A informada são:")

while qtdTermos <= 10:
    print(f"\t{qtdTermos:>2}º termo: {termoN:>2}", end= "")
    if qtdTermos % 2 == 0:
        print("")
    else:
        print("\t|", end="")
    termoN += razao
    qtdTermos += 1