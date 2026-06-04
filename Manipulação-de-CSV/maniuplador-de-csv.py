from defs.menu.menus import menu, título_simples
from defs.manipulacao_csv.manipulacaocsv import verificar_csv, criar_csv, exibir_arquivo, adicionar_linha_csv, editar_linha_csv

menu_1 = ('CRIAR ARQUIVO', 'EDITAR ARQUIVO','EXIBIR ARQUIVO' , 'ENCERRAR')
menu_edicao = ('ADICIONAR LINHA', 'EDITAR LINHA')

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
            print('ERRO: Esse arquivo já existe!'.center(60))
            print('xxx'*20)
    elif opcao_user == 2:
        opcao2_user = menu('EDIÇÃO DE ARQUIVOS', menu_edicao)
        if opcao2_user == 1:
            nome_arquivo = str(input('Digite o nome do arquivo que deseja adicionr uma linha: ')).strip()
            numero_linhas = int(input('Quantas linhas deseja adicionar ao arquivo: '))
            adicionar_linha_csv(name_arq=nome_arquivo, num_linhas=numero_linhas)
        elif opcao2_user == 2:
            nome_arquivo = str(input('Digite o nome do arquivo que deseja fazer uma alteração: '))
            editar_linha_csv(nome_arq=nome_arquivo)
    elif opcao_user == 3:
        título_simples('EXIBIÇÃO DE ARQUIVOS')
        nome_arquivo = str(input('Digite o nome do arquivo que deseja exibir: ')).strip()
        exibir_arquivo(nome_arquivo)        
    elif opcao_user == 4:
        print('ENCERRANDO....')
        break

