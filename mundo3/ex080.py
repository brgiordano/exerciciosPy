# Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
print('-'*60)
print(f"{"Lista ordenada sem repetições":^60}")
print('-'*60)

valores = []
for i in range(5):
    valor = int(input('Digite um valor inteiro: '))
    posicao: int = 0

    if valores:
        for index, v in enumerate(valores):
            posicao = index
            if valor < v:
                valores.insert(posicao, valor)
                break
        else:  # else de for
            valores.append(valor)
            posicao +=1
    else: valores.append(valor)

    if posicao == 0:
        localizacao = "ao início"
    elif posicao == len(valores) - 1:
        localizacao = "ao fim"
    else:
        localizacao = f"na posição [{posicao}]"

    print(f"\033[3;36m\tValor adicionado {localizacao} da lista!\033[m")

print('-'*60)
print(f"Os valores adicionados foram {valores}")