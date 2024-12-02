from mundo3.ex115.bd.bd_manager import GerenciadorBD as Banco
from mundo3.ex115.utils.utils import header, get_opt, error_msg, print_line
from mundo3.ex115.utils.colors import Cores as Clr


def opt_3():
    header('EXCLUSÃO DE CADASTRO')

    cadastros = Banco.bd_obter_cadastros()
    if cadastros:
        while True:
            opt = get_opt('Número do castro [0 para cancelar]: ')
            try:
                opt = int(opt)
                if opt == 0:
                    break
                opt -= 1
                if 0 <= opt < len(cadastros):
                    nome, idade = cadastros[opt].split(';')
                    print_line()
                    print(
                        Clr.color_str('EXCLUINDO CADASTRO DE:','RED'),
                        Clr.color_str(f'\n\tNOME: {nome.strip()} - IDADE: {idade.strip()}', 'BLUE')
                    )
                    while True:
                        resp = get_opt('CONFIRMAR? [S/N]: ').upper()
                        if resp not in ['S','N']:
                            error_msg('Opção inválida! - Digite S ou N.')
                            continue
                        else:
                            if resp == 'S':
                                cadastros.pop(opt)
                                Banco.bd_refazer(cadastros)
                                print(Clr.color_str('\tCadastro EXCLUÍDO com sucesso!','GREEN'))
                            break
                    break
                else:
                    error_msg('Cadastro não localizado!')
            except ValueError:
                error_msg('Digite um valor inteiro válido!')
    else:
        print(Clr.color_str('\tNão há pessoas cadastradas.', 'BLUE'))





    # Banco.bd_excluir(index)
