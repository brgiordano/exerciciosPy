# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
print('-'*80)
print(f"{"Tabuada de multiplicação":^60}")
print('-'*80)
while True:
    numero = int(input('Digite o valor da tabuada que deseja exibir [valor negativo para finalizar]: '))
    if numero < 0:
        break
    for c in range(1, 11):
        print(f'\t{numero} x {c:>2} = {numero*c:>2}')
    print('-'*80)

print('-'*80)
print("Programa finalizado!")