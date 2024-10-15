# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metros = float(input("Digite uma distância em metros(m): "))
print(f"A medida de {metros}m corresponde a:")
print(f"\t{metros/1000}km")
print(f"\t{metros/100}hm")
print(f"\t{metros/10}dam")
print(f"\t{metros*10}dm")
print(f"\t{metros*100}cm")
print(f"\t{metros*1000}mm")