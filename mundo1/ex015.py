# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

qtdDiasAlugado = int(input("Digite a quantidade de dias de aluguel: "))
kmPercorridos = float(input("Digite quantos km foram percorridos: "))
valorAluguel = qtdDiasAlugado*60 + kmPercorridos*0.15
print(f"O valor total do aluguel é de R${valorAluguel:.2f}")