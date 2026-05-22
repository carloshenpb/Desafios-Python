from exrc115.lib.Exibição import exibirusers
from lib import Exibição
from lib.Arquivo import *
from lib.Cadastro import cadastrodeusuers

arquivodetexto = 'lib/Arquivo/listadeusuarios.txt'
if not arquivoexiste(arquivodetexto):
    criararquivo(arquivodetexto)

while True:
    resposta = Exibição.menu(['\033[0;34m VER USUÁRIOS CADASTRADOS\033[m', '\033[0;34m CADASTRAR NOVO USUÁRIO\033[M', '\033[0;34m ENCERRAR PROGRAMA\033[m'])
    if resposta == 1:
        Exibição.cabecalho(f'{"\033[0;33m 01 - \033[m"}{"\033[0;34mVER USUÁRIOS CADASTRADOS\033[m"}', '==', center=60)
        exibirusers(arquivodetexto)
    elif resposta == 2:
        Exibição.cabecalho(f'{"\033[0;33m 02 - \033[m"}{"\033[0;34m CADASTRAR NOVO USUÁRIO\033[m"}', '==', center=60)
        cadastrodeusuers(arquivodetexto)
    elif resposta == 3:
        Exibição.cabecalho(f'{"\033[0;33m 03 - \033[m"}{"\033[0;34m ENCERRAR PROGRAMA\033[m"}', '++', center=60 )
        Exibição.cabecalho('\033[0;31mENCERRANDO O PROGRAMA! OBRIGADO E VOLTE SEMPRE!\033[m', center=60)
        break
    else:
        print('\033[0;31mOpção inválida! Tente novamente com uma opção válida.\033[m')