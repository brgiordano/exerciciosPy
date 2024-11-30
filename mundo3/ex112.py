# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imput(),
# mas com uma validação de dados para aceitar apenas valores que seja monetários.
from utilidades import moeda, dado

print('-'*60)
print(f"{"Entrada de dados monetarios":^60}")
print('-'*60)

valor = dado.leia_dinheiro("Digite o preço R$: ")
moeda.resumo(valor, 10, 20)

