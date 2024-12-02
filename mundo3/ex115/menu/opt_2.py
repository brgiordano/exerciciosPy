from mundo3.ex115.utils.utils import header, error_msg, print_line
from mundo3.ex115.bd.bd_manager import GerenciadorBD as Banco
from mundo3.ex115.utils.colors import Cores as Clr

# cadastrar nova pessoa
def opt_2():
    header('NOVO CADASTRO')

    while True:
        nome = input('Digite o nome: ')
        idade = None
        while True:
            try:
                idade = abs(int(input('Digite a idade: ')))
                break
            except ValueError:
                error_msg('Digite um número inteiro válido!')
                continue
        print_line()
        print(
            Clr.color_str('NOVO CADASTRO:\n', 'GREEN'),
            Clr.color_str(f'\tNOME: {nome} - '
                               f'IDADE: {idade}',
                          'BLUE')
        )
        print('Os dados estão corretos?')

        for i, opt in enumerate(['CONFIRMAR', 'CORRIGIR', 'CANCELAR CADASTRO']):
            print(Clr.color_str(f'\t{i+1} - {opt}', 'CYAN'))

        while True:
            try:
                resposta = int(input('Resposta: '))
                if resposta not in [1, 2, 3]:
                    error_msg('Opção inválida!')
                    continue
                break
            except ValueError:
                error_msg('Digite um número inteiro válido!')
        match resposta:
            case 1:
                pessoa = (nome, idade)
                Banco.bd_cadastrar(pessoa)
                print(Clr.color_str(f'\tCadastrado com sucesso!', 'GREEN'))
                break
            case 2:
                continue
            case 3:
                break