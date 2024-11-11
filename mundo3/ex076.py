# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
print('-'*60)
print(f"{"Produtos e preços em Tupla":^60}")
print('-'*60)

produtos = (
    "Lápis", 1.75, "Borracha", 2.00,
    "Caderno", 15.00, "Estojo", 12.00,
    "Caneta", 3.50, "Mochila", 85.00,
    "Livro", 42.00, "Régua", 4.25,
    "Marca-texto", 5.75, "Calculadora", 39.90,
    "Apontador", 2.50, "Tesoura", 6.50,
    "Compasso", 9.00, "Cola", 3.00,
    "Pincel", 7.20, "Aquarela", 18.90,
    "Papel A4", 12.00, "Fichário", 21.00,
    "Transferidor", 3.90, "Agenda", 10.00,
    "Giz de Cera", 8.50, "Corretivo", 4.30
)

print('='*47)
print(f"{"LISTAGEM DE PREÇOS":^47}")
print('='*47)
for i, j in enumerate(produtos):
    if i%2 == 0:
        print(f"\t{j:.<30}", end="")
    else:
        print(f"R$ {j:>6.2f}")
