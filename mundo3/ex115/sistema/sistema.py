from mundo3.ex115.menu.menu import Menu
from mundo3.ex115.utils.utils import get_opt, error_msg

class Sistema:

    @staticmethod
    def start():

        sys_exit = False
        while not sys_exit:
            Menu.exibir()

            while True:
                opt = get_opt('Sua opção: ').strip()
                if opt.isdigit():
                    match opt:
                        case '1':
                            Menu.opcao_1()
                        case '2':
                            Menu.opcao_2()
                        case '3':
                            Menu.opcao_3()
                        case '4':
                            Menu.opt_exit()
                            sys_exit = True
                            break
                        case _:
                            error_msg('Opção inválida!')
                            continue
                else:
                    error_msg('Digite um número inteiro válido!')
                    continue
                break