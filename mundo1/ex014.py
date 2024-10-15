# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input("Digite uma temperatura em graus Celsius (ºC): "))
print(f"A temperatura de {celsius:.1f}ºC corresponde a {1.8*celsius + 32:.1f}ºF (Fahrenheit)")