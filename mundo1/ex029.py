# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
velocidadeMax: float = 80
velocidadeCarro = float(input("Digite a velocidade do carro (km/h): "))
multa: float = 0
if velocidadeCarro > velocidadeMax:
    multa = (velocidadeCarro-velocidadeMax)*7
    print("Você foi multado por ultrapassar o limite de velocidade.\n"
          f"\tVelocidade máxima permitida: {velocidadeMax}km/h\n"
          f"\tVelocidade auferida: {velocidadeCarro}km/h\n"
          f"\tValor da multa: R${multa:.2f}")
print("Tenha um bom dia. Dirija com segurança!")