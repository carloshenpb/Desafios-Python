from defs.menus.menus import menu_completo, título_simples
from defs.dados_api.api_dados import adicionar_cnpj

menu1_opcs = ['Buscar CNPJ', 'Exibir lista de CNPJ', 'Filtrar CNPJs', 'Adicionar dados manualmente', 'Editar dado manualmente', 'Sair']
menu1_name = 'Buscador de CNPJ'
menu2_opcs = ['Exibição simples', 'Exibição em tabela']


while True:
    menu1 = menu_completo(nome_do_menu = menu1_name, opcoes = menu1_opcs)
    if menu1 == 6:
        print('SAINDO.....')
        break
    elif menu1 == 1:
        título_simples('BUSCAR CNPJs')
        cnpj_user = str(input('Digite um CNPJ válido: '))
        adicionar_cnpj(cnpj_user)
    elif menu1 == 2:
        print('exibições')
    elif menu1 == 3:
        print('filtros')
    elif menu1 == 4:
        print('adicionar dados de forma manual')
    elif menu1 == 5: 
        print('editar dados manualmente')
    