# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
#   A) Quantos números foram digitados.
#   B) A lista de valores, ordenada de forma decrescente.
#   C) Se o valor 5 foi digitado e está ou não na lista.
print('-'*60)
print(f"{"Extraindo dados de uma lista":^60}")
print('-'*60)

numeros = []
while True:
    numero = input('Digite um numero inteiro [\'S\' para SAIR]: ')
    try:
        numeros.append(int(numero))
        print("\033[3;36m\tValor adicionado!\033[m")
    except ValueError:
        if numero.upper() == 'S':
            break
        else: print("\033[3;31m\tValor inválido!\033[m")
print('-'*60)
print(f"Foram digitados {len(numeros)} números.\n"
      f"Os números na ordem decrescente foram: {sorted(numeros, reverse=True)}\n"
      f"O valor 5 {"está" if 5 in numeros else "não está"} na lista.")
