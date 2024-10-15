# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
desconto = 0.05
preco = float(input("Informe o preço do produto (R$): "))
print(f"Valor de R${preco:.2f} com desconto de 5% fica por R${preco*(1-desconto):.2f}")