# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas
# os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
print('-'*60)
print(f"{"Lista ordenada sem repetições":^60}")
print('-'*60)
lista = []
while True:
    valor = input("Digite um valor inteiro [\'S\' para SAIR]: ")
    try:
        lista.append(int(valor))
        print(f"\033[3;36m\tValor adicionado!\033[m")
    except ValueError:
        if valor.upper() == 'S':
            break
        else: print(f"\033[3;31m\tValor inválido!\033[m")

lista_pares = [p for p in lista if p % 2 == 0]
lista_impares = [i for i in lista if i%2 != 0]
print('-'*60)
print(f"A lista original é: {lista}\n"
      f"Os valores pares são: {lista_pares}\n"
      f"Os valores impares são: {lista_impares}")