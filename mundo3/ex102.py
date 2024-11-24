# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular
# e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
print('-'*60)
print(f"{"Função para fatorial":^60}")
print('-'*60)
def fatorial(val: int, show=False):
    """
    Calcula o fatorial de um número inteiro não negativo e retorna o resultado.
    :param val: valor inteiro não negativo que será usado para o cálculo.
    :param show: (opt) False(default), True: Exibe o cálculo do fatorial.
    :return: resultado do fatorial: int.
    """
    if val < 0:
        raise ValueError('Informe um valor inteiro não negativo.')

    if show:
        if val == 0:
            print("[def]: ", end='')
        print(f"fat({val}) = ", end='')

    fat = 1
    for v in range(val, 0, -1):
        fat *= v
        if show:
            if val > 1:
                print(f"{v}x" if v>1 else f"{v} = ", end='')
    return fat

print(fatorial(0, True))
print(fatorial(1, True))
print(fatorial(5, True))
print(fatorial(6))
print(help(fatorial))