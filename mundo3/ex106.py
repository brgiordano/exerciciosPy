# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use colors.
import shutil

def pyhelp():
    # captura a largura do terminal
    largura_terminal = shutil.get_terminal_size().columns
    def cabecalho1():
        print('\33[1;30;42m' + f"{'~' * largura_terminal}")
        print(f"{'SISTEMA DE AJUDA PyHELP':^{largura_terminal}}")
        print('~' * largura_terminal, '\33[m')

    def cabecalho2():
        print('\33[30;43m' + '~' * largura_terminal)
        print(f"{f"Acessando manual do comando '{nome}'":^{largura_terminal}}")
        print('~' * largura_terminal, '\33[m')

    def fim():
        print('\33[1;30;44m' + '~' * largura_terminal)
        print(f"{f"Até logo!":^{largura_terminal}}")
        print('~' * largura_terminal, sep='')

    while True:
        cabecalho1()
        nome = input("Nome da função ou da bibioteca Python ('fim' para sair): ").strip().lower()

        if nome == 'fim':
            fim()
            break

        cabecalho2()
        print('\033[30;48;5;15m')
        help(nome)
        print('\033[m', end='')

    print('\033[m',end='')

pyhelp()