from defs.menu.menus import menu, título_simples
from defs.manipulacao_csv.manipulacaocsv import verificar_csv, criar_csv

menu_1 = ('CRIAR ARQUIVO', 'EDITAR ARQUIVO','EXIBIR ARQUIVO' , 'ENCERRAR')

while True:
    opcao_user = menu(nome_do_menu='MANIPULADOR DE CSV', opcoes=menu_1)   
    if opcao_user == 1:
        título_simples('CRIAÇÃO DE ARQUIVO')
        nome_arquivo = str(input('Digite o nome que deseja por no arquivo: ')).strip()
        if not verificar_csv(nome_arquivo):
            numero_colunas = int(input('Digite a quantidade de colunas que deseja: '))
            criar_csv(nome_arq=nome_arquivo, num_col=numero_colunas)
        else:
            print('xxx'*20)
            print('ERRO: Esse arquivo já existe!')
            print('xxx'*20)
    elif opcao_user == 4:
        print('ENCERRANDO....')
        break

