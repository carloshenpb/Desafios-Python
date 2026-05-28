from menu.menu_editavel import menu
from arquivo.manipulação_de_csv import criar_csv, adicionar_linha_csv

opcs = ['Criar arquivo', 'Editar arquivo', 'Exibir arquivo', 'Verificar arquivo' , 'Encerrar']
while True:
    menu_1 = menu('menu 1', opcs)
    if menu_1 == 5:
        print('ENCERRANDO......')
        break
    elif menu_1 == 1:
        criar_csv()
    elif menu_1 == 2:
        opcs_2 = ['Adicionar linha', 'Editar linha']
        menu_2 = menu('menu 2', opcs_2)
        if menu_2 == 1:
            arquivo_nome = str(input('Digite o nome do arquivo: '))
            adicionar_linha_csv(arquivo_nome)  
        elif menu_2 == 2:
            arquivo_nome = str(input('Digite o nome do arquivo que deseja editar: '))
            linha_edit = str(input())  