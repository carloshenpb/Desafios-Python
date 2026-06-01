def menu (nome_do_menu = 'Menu 1', opcoes = ('Opção 1', 'Opção 2', 'Opção 3')):
    """
Exibe um menu estilizado no terminal, lê a opção escolhida pelo usuário e retorna o valor.
Garante que a entrada seja um número inteiro válido e pertencente ao intervalo de opções.

Argumentos:
    nome_do_menu (str): O título que será exibido no topo do menu.
    opcoes (tuple): Uma tupla de strings representando as opções disponíveis.

Retorna:
    int: O número da opção válida digitada pelo usuário.
"""
    print('___'*20)
    print(f'{nome_do_menu}'.center(60))
    print ('___'*20)
    for num, op in enumerate(opcoes, start=1):
        print(f'[{num}° - {op}]'.center(60))
    print('___'*20)
    while True:
        try:
            opcao = int(input('Digite a opção que deseja: '))
            if opcao < 1 or opcao > len(opcoes):
                raise ValueError
        except ValueError:
            print('ERRO: Opção invália! Digite o número da opção que deseja.')
            continue
        else:
            break
    return opcao

def título_simples(nome_menu):
    print('==='*20)
    print(nome_menu.center(60))
    print('==='*20)