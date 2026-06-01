from defs.menu.menus import menu

menu_1 = ('CRIAR ARQUIVO', 'EDITAR ARQUIVO', 'ENCERRAR')

while True:
    opcao_user = menu(nome_do_menu='MANIPULADOR DE CSV', opcoes=menu_1)
    if opcao_user == 3:
        print('ENCERRANDO....')
        break