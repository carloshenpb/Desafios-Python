import urllib.request
from urllib.error import URLError

try:
    site = urllib.request.urlopen('https://pudim.com.br/')
except URLError:
    print('\033[0;31mO Site\033[m \033[0;36mhttps://pudim.com.br/\033[m \033[0;31mnão está acessível!\033[m')
else:
    print('\033[0;33mO Site \033[m\033[0;36mhttps://pudim.com.br/\033[m \033[0;33mestá acessível!\033[m')
    print(site.read())