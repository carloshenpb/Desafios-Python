from defs.menu.menus import menu, título_simples
from defs.manipulacao_csv.manipulacaocsv import verificar_csv, criar_csv

menu_1 = ('CRIAR ARQUIVO', 'EDITAR ARQUIVO','EXIBIR ARQUIVO' , 'ENCERRAR')

while True:
    opcao_user = menu(nome_do_menu='MANIPULADOR DE CSV', opcoes=menu_1)
    
    if opcao_user == 1:
        título_simples('CRIAÇÃO DE ARQUIVO')
        while True:
            nome_arquivo = str(input('Digite o nome que deseja por no arquivo: ')).strip()
            testando_arq = verificar_csv(nome_arquivo)
            if testando_arq == False:
                print(f'ERRO: este arquivo já existe!')
                break
            numero_colunas = int(input('Digite o número de colunas que deseja que o arquivo tenha: '))
            criar_csv(nome_arq = nome_arquivo, num_col = numero_colunas )

    elif opcao_user == 3:
        título_simples('EXIBIÇÃO DE ARQUIVO')
        nome_arquivo = str(input('Digite o nome do arquivo que deseja exibir: '))
        
    elif opcao_user == 4:
        print('ENCERRANDO....')
        break

