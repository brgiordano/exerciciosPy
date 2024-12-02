from mundo3.ex115.menu.opt_1 import opt_1
from mundo3.ex115.menu.opt_2 import opt_2
from mundo3.ex115.menu.opt_3 import opt_3
from mundo3.ex115.utils.utils import header, print_line
from mundo3.ex115.utils.colors import Cores as Clr


class Menu:
    @staticmethod
    def exibir():
        header('MENU PRINCIPAL')

        menu = ['Ver pessoas cadastradas',
                'Cadastrar nova pessoa',
                'Sair do sistema']
        for i, item in enumerate(menu):
            print(Clr.color_str(f'\t{i + 1} - {item}', 'CYAN'))
        print_line()

    @staticmethod
    def opcao_1():
        opt_1()

    @staticmethod
    def opcao_2():
        opt_2()

    @staticmethod
    def opt_exit():
        opt_3()