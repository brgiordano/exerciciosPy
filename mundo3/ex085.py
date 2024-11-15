# Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
print('-'*60)
print(f"{"Lista com pares e ímpares":^60}")
print('-'*60)

par_impar = [[],[]]
for i in range (7):
    num = int(input(f"Digite o {i+1}º valor inteiro: "))
    if num % 2 == 0:
        par_impar[0].append(num)
    else:
        par_impar[1].append(num)

par_impar[0].sort()
par_impar[1].sort()
print('-'*60)

print(f"Os valores pares digitados foram: {par_impar[0]}.\n"
      f"Os valores ímpares digitados foram: {par_impar[1]}")