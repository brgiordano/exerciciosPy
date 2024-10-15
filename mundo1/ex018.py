# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = float(input("Digite um ângulo: "))
print(f"O Seno do ângulo de {angulo}º é: {math.sin(math.radians(angulo)):.3f}\n"
      f"O Cosse do ângulo de {angulo}º é: {math.cos(math.radians(angulo)):.3f}\n"
      f"A Tangente do ângulo de {angulo}º é: {math.tan(math.radians(angulo)):.3f}")