# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
# DESAFIO 61:
#       # Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
#       # mostrando os 10 primeiros termos da progressão usando a estrutura while.
#       # DESAFIO 51:
#               # Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#               # No final, mostre os 10 primeiros termos dessa progressão.
print('-'*30)
print(f"{"Progressão Aritmética":^30}")
print('-'*30)

primeiro_termo = int(input("Digite o primeiro termo da P.A: "))
razao = int(input("Digite a razão da P.A: "))
termoN = primeiro_termo
qtdTermos = 10
contador_termos = 1
identacao = contador_termos

print("Os 10 primeiros termos da P.A são:")
while contador_termos <= qtdTermos:
    print(f"\t{contador_termos:>2}º termo: {termoN:>2}", end="")
    termoN += razao
    if identacao % 2 != 0 and contador_termos < qtdTermos:
        print("\t|", end="")
    else: print("")

    if contador_termos == qtdTermos:
        print("\nSe deseja continuar, digite a quantidade de termos a mais que deseja exibir.")
        while True:
            novosTermos = int(input("Quantos termos deseja exibir [digite 0 para finalizar]: "))
            if novosTermos > 0:
                print(f"Os próximos {novosTermos} termos da P.A são:")
                qtdTermos += novosTermos
                identacao = 0
                break
            elif novosTermos == 0:
                break
            else:
                print("Valor inválido! Digite um valor não negativo!")
    contador_termos += 1
    identacao += 1
print(f"A progressão foi finalizada com {qtdTermos} termos exibidos.")
