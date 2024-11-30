# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib.request
from urllib.error import URLError
print('-'*60)
print(f"{"Testando se um site está acessível":^60}")
print('-'*60)

site = 'https://www.google.org'
try:
    resposta = urllib.request.urlopen(site)
    print("\33[32m",f"O site '{site}' está ACESSÍVEL!","\33[m", sep='')
except URLError:
    print("\33[31m",f"O Site {site} está INACESSÍVEL!","\33[m", sep='')
