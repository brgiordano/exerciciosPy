# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('-'*60)
print(f"{"Caixa eletrônico":^60}")
print('-'*60)

cedulas50: int = 0
cedulas20: int = 0
cedulas10: int = 0
cedulas1: int = 0
while True:
    try:
        valor_saque = int(input("Digite o valor do saque: R$ "))
        if valor_saque < 0:
            print("Valor não pode ser negativo!")
        else: break
    except ValueError:
        print("Valor inválido!")

aux = valor_saque
cedulas50 = aux//50
aux %= 50

cedulas20 = aux//20
aux %= 20

cedulas10 = aux//10
aux %= 10

cedulas1 = aux

print('*'*60)
print(f"Você sacou R${valor_saque:.2f}")
print(f"\t{cedulas50:>2} cédulas de R$ 50,00\n" if cedulas50 > 0 else '', end='')
print(f"\t{cedulas20:>2} cédulas de R$ 20,00\n" if cedulas20 > 0 else '', end='')
print(f"\t{cedulas10:>2} cédulas de R$ 10,00\n" if cedulas10 > 0 else '', end='')
print(f"\t{cedulas1:>2} cédulas de R$ 1,00\n" if cedulas1 > 0 else '', end='')
print('*'*60)

