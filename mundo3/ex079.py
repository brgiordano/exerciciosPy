# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

print('-'*60)
print(f"{"Valores únicos em uma Lista":^60}")
print('-'*60)

valores = []
while True:
    valor = input('Digite um valor inteiro [\'F\' para finalizar]: ')
    try:
        valor = int(valor)
        if valor not in valores:
            valores.append(int(valor))
            print(f"\t{'\033[32m'}Valor adicionado!{'\033[m'}")
        else:
            print(f"\t{'\033[33m'}Valor duplicado [não adicionado].{'\033[m'}")
    except ValueError:
        if valor.upper() != 'F':
            print(f"\t{'\033[31m'}Valor inválido!{'\033[m'}")
        else: break

print('-'*60)
if valores:
    print(f"Os valores digitados, em ordem crescente, foram: {sorted(valores)}")
else: print("Nenhum valor foi digitado!")
