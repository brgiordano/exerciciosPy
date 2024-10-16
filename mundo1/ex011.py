# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larguraParede = float(input("Largura da parede em metros(m): "))
alturaParede = float(input("Altura da parede em metros(m): "))
areaParede = larguraParede * alturaParede
litroTintaNecessario = areaParede/2
print(f"Sua parede em as dimensões de {larguraParede:.2f}m x {alturaParede:.2f}m com área total de {areaParede:.2f}m²")
print(f"Você precisará de {litroTintaNecessario:.2f} litros de tinta para pintar toda a parede.")