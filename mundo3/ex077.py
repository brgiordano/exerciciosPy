# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
print('-'*60)
print(f"{"Contagem de voagis em Tupla":^60}")
print('-'*60)

palavras = (
    "zxc","livro", "computador", "mesa", "cadeira", "teclado",
    "janela", "porta", "telefone", "caderno", "caneta",
    "papel", "faca", "garfo", "prato", "colher",
    "copo", "garrafa", "luz", "quadro", "parede"
)
for p in palavras:
    print(f"\t{p}: {sum(p.upper().count(vog) for vog in "AEIOU")} vogais", end='')

    vogais_palavra = [letra.upper() for letra in p if letra.upper() in "AEIOU"]

    print(f" ({", ".join(vogais_palavra)})") if vogais_palavra else print('')