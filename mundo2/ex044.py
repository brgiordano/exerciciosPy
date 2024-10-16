# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

print("-=-"*20)
print("CÁLCULO DE E PREÇO".center(60))
print("-=-"*20)

preco = float(input("Preço das compras R$ "))
while True:
    print(
        '''FORMAS DE PAGAMENTO:
        [1] - À vista (Dinheiro / Cheque)
        [2] - À vista (Cartão)
        [3] - 2x (Cartão)
        [4] - 3x ou mais (Cartão)
        [0] - CANCELAR''')
    formaPagamento = int(input("Escolha a forma de pagamento: "))
    if 0 <= formaPagamento < 5: break
    else: print("\tOpção INVÁLIDA!\n")

msgValor = f"Sua compra no valor de R${preco:.2f}"
match formaPagamento:
    case 1:
        print(msgValor + ", com desconto de 10%, ficará por R${:.2f}".format(0.90 * preco))
    case 2:
        print(msgValor + ", com desconto de 5%, ficará por R${:.2f}".format(0.95 * preco))
    case 3:
        print(msgValor, "será parcelada, SEM JUROS, em 2x de R${:.2f}".format(preco/2))
    case 4:
        while True:
            qtdParcelas = int(input("\tQuantidade de parcelas (min 3 | max 10): "))
            if qtdParcelas == 0:
                print("Operação CANCELADA.")
                exit(0)
            if 2 < qtdParcelas <= 10: break
            else: print("Escolha entre 3 e 10 parcelas ou digite 0 para cancelar a operação.")
        print(msgValor, f"será parcelada, COM JUROS, em {qtdParcelas}x de R${(preco * 1.2) / qtdParcelas:.2f}"
                        f"\nFicando um valor final de R${preco * 1.2:.2f}")