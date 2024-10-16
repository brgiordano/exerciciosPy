# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

print("-=-"*20)
print("Cálculo de IMC".center(60))
print("-=-"*20)

massa = float(input("\tDigite seu peso(kg): "))
altura = float(input("\tDigite sua altura(m): "))
imc = massa / (altura ** 2)

print(f"IMC: {imc:.1f} - ", end="")
if imc < 18.5:
    print("ABAIXO DO PESO.")
elif 18.5 <= imc < 25:
    print("PESO IDEAL.")
elif 25 <= imc < 30:
    print("SOBREPESO.")
elif 30 <= imc <= 40:
    print("OBESIDADE.")
else:
    print(f"IMC: {imc:.1f} - OBESIDADE MÓRBIDA.")