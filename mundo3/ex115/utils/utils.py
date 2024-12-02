from mundo3.ex115.utils import Cores as Clr

def header(title):
    print('-'*45,
              f'\n{f"{title}":^45}\n',
          '-'*45, sep='')

def error_msg(msg):
    print(Clr.color_str(msg, 'RED'))

def get_opt():
    opt = input(Clr.color_str('Sua opção: ', 'YELLOW'))
    return opt

def print_line(num = 45):
    print('-'*45)