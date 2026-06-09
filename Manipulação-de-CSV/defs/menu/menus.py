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
            print('ERRO: Opção inválida! Digite o número da opção que deseja.')
            continue
        else:
            break
    return opcao

def título_simples(nome_menu):
    """
Exibe um título centralizado no terminal, emoldurado por linhas decorativas.

Argumentos:
    nome_menu (str): O texto que será exibido como título.
"""
    print('==='*20)
    print(nome_menu.center(60))
    print('==='*20)

def so_opcoes (opcoes = ('Opção 1', 'Opção 2', 'Opção 3')):
    """
    Exibe um menu de opções numeradas e centralizadas, lê a escolha do usuário 
    e garante a entrega de um valor inteiro correspondente a uma opção válida.

    Argumentos:
        opcoes (tuple, opcional): Uma tupla de strings contendo os nomes das opções. 
                                  O padrão é ('Opção 1', 'Opção 2', 'Opção 3').

    Retorna:
        int: O número correspondente à opção válida selecionada pelo usuário.
    """
    print('___'*20)
    for num, op in enumerate(opcoes, start=1):
        print(f'[{num}° - {op}]'.center(60))
    print('___'*20)
    while True:
        try:
            opcao = int(input('Digite a opção que deseja: '))
            if opcao < 1 or opcao > len(opcoes):
                raise ValueError
        except ValueError:
            print('ERRO: Opção inválida! Digite o número da opção que deseja.')
            continue
        else:
            break
    return opcao