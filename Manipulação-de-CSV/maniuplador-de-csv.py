from defs.menu.menus import menu, título_simples
from defs.manipulacao_csv.manipulacaocsv import verificar_csv

menu_1 = ('CRIAR ARQUIVO', 'EDITAR ARQUIVO', 'ENCERRAR')

while True:
    opcao_user = menu(nome_do_menu='MANIPULADOR DE CSV', opcoes=menu_1)
    
    if opcao_user == 1:
        título_simples('CRIAÇÃO DE ARQUIVO')
        nome_arquivo = input('Digite um nome para o arquivo que deseja criar: ')
        testando_arq = verificar_csv(nome_arquivo)
    elif opcao_user == 3:
        print('ENCERRANDO....')
        break

