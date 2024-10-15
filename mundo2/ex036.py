# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
qtdAnos = int(input("Tempo de financiamento (anos): "))
qtdMeses = qtdAnos * 12
parcela = valorCasa/qtdMeses
if parcela/salario <= 0.3:
    emprestimoConcedido = True
else:
    emprestimoConcedido = False

print("-=-"*20)
print("\tValor da casa: R${:.2f}\n"
      "\tQuantidade de prestações: {}\n"
      "\tValor da parcela: R${:.2f}\n"
      "\tEmpréstimo {}"
      .format(valorCasa, qtdMeses, parcela, "CONCEDIDO!" if emprestimoConcedido else "NEGADO!"))
print("-=-"*20)

