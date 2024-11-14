# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
print('-'*60)
print(f"{"Maior e menor valores em lista":^60}")
print('-'*60)


valores = []
for i in range(0,5):
    while True:
        try:
            valor_recebido = int(input(f"\tDigite um valor inteiro pos[{i}]: "))
            valores.append(valor_recebido)
            break
        except ValueError:
            print("Valor incorreto!")

maior_valor = max(valores)
posicoes_maior_valor = [str(index) for index, valor in enumerate(valores) if valor == maior_valor]
print(f"O maior valor digitado foi {maior_valor}", end='')
print(f" na posição [{", ".join(posicoes_maior_valor)}]")

menor_valor = min(valores)
posicoes_menor_valor = [str(index) for index, valor in enumerate(valores) if valor == menor_valor]
print(f"O menor valor digitado foi {min(valores)}", end='')
print(f" na posição [{", ".join(posicoes_menor_valor)}]")