# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o valor do salário: R$"))
aumento: float
if salario > 1250:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15
print(f"O valor do aumento foi de R${aumento:.2f}\n"
      f"O novo valor do salário será de R${salario+aumento:.2f}")