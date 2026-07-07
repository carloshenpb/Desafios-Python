from funções import funcoes_menu
menu_opcs = ['Criar Lista', 'Adicionar Linha','Editar Linha', 'Exibir Lista Ordenada', 'Sair']

while True:
    menu = funcoes_menu.menu_completo(nome_do_menu="Listas ordenadas CSV", opcoes=menu_opcs)
    if menu == 5:
        print('SAINDO............')
        break
    elif menu == 1:
        pass
    elif menu == 2:
        pass
    elif menu == 3:
        pass
    elif menu == 4:
        pass