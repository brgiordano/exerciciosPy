# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’) Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~
print('-'*60)
print(f"{"Um print especial":^60}")
print('-'*60)

def escreva(msg):
    tamanho = len(str(msg)) + 4
    print('~' * tamanho)
    print(f"{msg:^{tamanho}}")
    print('~' * tamanho)

escreva("Olá mundo!")
escreva("Hello world!")
escreva("Fim do programa!")