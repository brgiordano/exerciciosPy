# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
print('-'*60)
print(f"{"Cálculo de área de terreno":^60}")
print('-'*60)

def area(l, c):
    return l * c

print(f"{"Área de terreno":^20}")
print('='*20)
largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))
print(f"A área de um terreno de {largura:.1f}m x {comprimento:.1f}m é de {area(largura,comprimento):.2f}m²")
