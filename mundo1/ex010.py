# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
import time

valorEmReal = float(input("Digite o valor em R$ para ser convertido em U$: "))
# cotacaoDolarEmReal = 5.48
cotacaoDolarEmReal = 3.27
for i in range(51):
    print(f"\rProgresso: [{('#' * i).ljust(50)}] {i*2}% ", end="")
    time.sleep(0.1)
print(f"\nCom R${valorEmReal:.2f} você pode comprar U${valorEmReal/cotacaoDolarEmReal:.2f}")