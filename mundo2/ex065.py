# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
print('-'*60)
print(f"{"Média dos números":^60}")
print('-'*60)

numeros: [int] = []
continuar = True

while continuar:
    numero = int(input("\tDigite um valor inteiro: "))
    numeros.append(numero)

    while continuar:
        resposta = str(input("Deseja continuar? [S/N]: ")).upper().strip()
        if resposta == 'S':
            break
        elif resposta == 'N':
            continuar = False
            break
        else:
            print("Resposta inválida. Digite [S] para SIM ou [N] para NÃO.")
print("-"*60)
print(f"Você digitou {len(numeros)} numéros, e a média deles foi {sum(numeros) / len(numeros)}.\n"
      f"O maior número digitado foi {max(numeros)}, e o menor foi {min(numeros)}.")