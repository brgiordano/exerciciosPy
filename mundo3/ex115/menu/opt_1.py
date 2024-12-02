from mundo3.ex115.utils.utils import header
from mundo3.ex115.bd.bd_manager import GerenciadorBD as Banco
from mundo3.ex115.utils.colors import Cores as Clr

# ver pessoas cadastradas
def opt_1():
    header('PESSOAS CADASTRADAS')
    if not Banco.bd_view():
        print(Clr.color_str('\tNão há pessoas cadastradas', 'BLUE'))