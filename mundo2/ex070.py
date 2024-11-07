# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#   A) qual é o total gasto na compra.
#   B) quantos produtos custam mais de R$1000.
#   C) qual é o nome do produto mais barato.
print('-'*60)
print(f"{"Estatísticas em produtos":^60}")
print('-'*60)

produtos = {}
while True:
    print("Cadastrando novo produto.")
    nome = str(input("\tNome do produto: "))
    while True:
        try:
            preco = float(input("\tPreço do produto: R$"))
            if preco < 0:
                print("Preço não pode ser negativo.")
            else: break
        except ValueError:
            print("Valor inválido para preço.")

    produtos[nome] = preco

    while True:
        continuar = input("Deseja continuar? [S/N]: ").strip().upper()
        if continuar not in ['S', 'N']:
            print("Resposta inválida. Digite 'S' para sim ou 'N' para não.")
        else: break
    if continuar == 'N': break
total = sum(produtos.values())
qtd_prod_maiores_que_mil = 0
nome_produto_mais_barato = min(produtos, key=produtos.get)
preco_produto_mais_barato = min(produtos.values())

for i in produtos.values():
    if i > 1000:
        qtd_prod_maiores_que_mil += 1
print('-'*60)
print(f"\tO total gasto na compra foi de R${total:.2f}\n"
      f"\t{qtd_prod_maiores_que_mil} produtos custam mais de R$1000.\n"
      f"\tO produto mais barato é '{nome_produto_mais_barato}' que custa, R${preco_produto_mais_barato:.2f}")

