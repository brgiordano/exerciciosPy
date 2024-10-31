# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
print(10*"-=-")
opcao = 0
while opcao != 5:
    print("\t[1] somar\n"
          "\t[2] multiplicar\n"
          "\t[3] maior\n"
          "\t[4] novos números\n"
          "\t[5] sair do programa")
    opcao = int(input("Escolha uma opção: "))
    match opcao:
        case 1:
            print(f"\tA soma entre {valor1} e {valor2} = {valor1 + valor2}")
        case 2:
            print(f"\tA mutliplicação entre {valor1} e {valor2} = {valor1 * valor2}")
        case 3:
            print(f"\tO maior valor entre {valor1} e {valor2} é {max(valor1, valor2)}")
        case 4:
            valor1 = float(input("Digite o primeiro valor: "))
            valor2 = float(input("Digite o segundo valor: "))
        case 5:
            break
        case _:
            print("\tValor invalido, tente novamente.")
    print(10 * "-=-")
print("Fim do programa")
