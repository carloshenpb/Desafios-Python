from defs.menus.menus import menu_completo, título_simples
from defs.dados_api.api_dados import adicionar_cnpj
from defs.manipulacao_de_json.defs_json import exibir_json_simples, exibir_json_tabela, filtrar_cnpj_especifico, filtros_json_padrao, adicionar_dados_json, edicao_dados_cnpj

menu1_opcs = ['Buscar CNPJ', 'Exibir lista de CNPJ', 'Filtrar CNPJs', 'Editar dados manualmente', 'Sair']
menu1_name = 'BUSCADOR DE CNPJ'
menu2_opcs = ['Exibição simples', 'Exibição em tabela']
menu3_opcs = ['Filtrar dados de um unico CNPJ', 'Outros Filtros']
menu4_opcs = ['Adicionar Empresa Manualmente', 'Editar dados de CNPJ existente']

while True:
    menu1 = menu_completo(nome_do_menu = menu1_name, opcoes = menu1_opcs)
    if menu1 == 5:
        print('SAINDO.....')
        break
    elif menu1 == 1:
        título_simples('BUSCAR CNPJs')
        cnpj_user = str(input('Digite um CNPJ válido: '))
        adicionar_cnpj(cnpj_user)
    elif menu1 == 2:
        menu2 = menu_completo('EXIBIÇÃO DE CNPJs', menu2_opcs)
        if menu2 == 1:
            título_simples('Exibição simples')
            exibir_json_simples()
        elif menu2 == 2:
            título_simples('Exibição tabular')
            exibir_json_tabela()
    elif menu1 == 3:
        menu3 = menu_completo('FILTROS DE CNPJ', menu3_opcs)
        if menu3 == 1:
            cnpj_user = str(input('Digite um CNPJ: '))
            filtrar_cnpj_especifico(cnpj_user)
        elif menu3 == 2:
            título_simples('Filtros padrões')
            filtros_json_padrao()
    elif menu1 == 4:
        menu4 = menu_completo('Edição Manual de Dados', menu4_opcs)
        if menu4 == 1:
            título_simples = ('Adição de Empresa')
            adicionar_dados_json()
        elif menu4 == 2:
            título_simples = ('Edição de dados')
            cnpj = str(input('Digite o CNPJ que deseja editar dados: '))
            edicao_dados_cnpj(cnpj)
