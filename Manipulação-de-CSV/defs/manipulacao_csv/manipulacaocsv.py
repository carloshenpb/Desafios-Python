from os.path import exists, join
import csv
from defs.menu.menus import so_opcoes

pasta_padrao = r'C:\Users\carlo\PycharmProjects\Desafios\Manipulação-de-CSV\arquivos'

def verificar_csv(arq_nome):
    """
    Verifica se um arquivo CSV já existe no diretório padrão do sistema.

    Argumentos:
        arq_nome (str): Nome do arquivo a ser verificado (sem a extensão .csv).

    Retorna:
        bool: True se o arquivo existir, False caso contrário.
    """
    arq_nome = arq_nome.strip()
    caminho_arquivo = join(pasta_padrao, f'{arq_nome}.csv')
    return exists(caminho_arquivo)
    
def criar_csv(nome_arq, num_col):
    """
    Cria um novo arquivo CSV com cabeçalhos personalizados informados pelo usuário,
    salvando-o diretamente na pasta padrão configurada globalmente.

    Argumentos:
        nome_arq (str): Nome do arquivo a ser criado (sem a extensão .csv).
        num_col (int): Quantidade de colunas que o arquivo terá.
    """
    nome_arq = nome_arq.strip()
    caminho_arquivo = join(pasta_padrao, f'{nome_arq}.csv')
    cabecalho = []
    for c in range(num_col):
        coluna = str(input(f'Digite o nome da {c+1}° coluna: '))
        cabecalho.append(coluna)
    try:
        with open(caminho_arquivo, "x", newline="", encoding="utf-8") as arquivo_novo:
            escritor = csv.DictWriter(arquivo_novo, fieldnames=cabecalho)
            escritor.writeheader()
    except Exception as erro:
        print(f'ERRO: {erro.__class__.__name__} : {erro}')
    else:
        print('Arquivo criado com sucesso!')

def exibir_arquivo(nome_arq):
    """
    Exibe o conteúdo de um arquivo CSV existente no diretório padrão,
    permitindo ao usuário escolher entre dois modos de exibição.

    Argumentos:
        nome_arq (str): Nome do arquivo a ser exibido (sem a extensão .csv).
    """
    nome_arq = nome_arq.strip()
    caminho_arquivo = join(pasta_padrao, f'{nome_arq}.csv')

    como_exibir = ('EXBIÇÃO SIMPLES', 'EXIBIÇÃO COM DICTREADER')
    modo_exibir = so_opcoes(como_exibir)

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo_lido:
            if modo_exibir == 1:
                leitor = csv.reader(arquivo_lido)
                for linha in leitor:
                    print(linha)
            elif modo_exibir == 2:
                leitor = csv.DictReader(arquivo_lido)
                linhas = list(leitor)
                if not linhas:
                    print('O arquivo está vazio, não possui linhas preenchidas nele!')
                else:
                    larguras = {
                    chave: max(len(chave), max(len(str(linha[chave])) for linha in linhas))
                    for chave in linhas[0].keys()
                    }
                    for num_linha, linha in enumerate(linhas, 1):
                        colunas = " | ".join(
                            f'{chave} : {str(valor):<{larguras[chave]}}'
                            for chave, valor in linha.items()
                            )
                        print(f'[{num_linha}° - linha]: {colunas}')            
    except Exception as erro:
        print(f'ERRO: {erro.__class__.__name__}: {erro}')

def adicionar_linha_csv(name_arq, num_linhas=1):
    """
    Adiciona uma ou mais linhas de dados a um arquivo CSV existente no diretório padrão.
    Lê o cabeçalho uma única vez para mapear as colunas e solicita as entradas ao usuário.

    Argumentos:
    name_arq (str): O nome do arquivo (sem a extensão .csv).
    num_linhas (int, opcional): A quantidade de linhas a serem adicionadas. O padrão é 1.
    """
    name_arq = name_arq.strip()
    caminho_arquivo = join(pasta_padrao, f'{name_arq}.csv')
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
                dados_cabecalho = csv.reader(arquivo)
                cabecalho = next(dados_cabecalho)

        for linha in range(1, num_linhas + 1):
            print(f'{linha}° linha: ')
            dados_linha = []
            for num_col, coluna in enumerate(cabecalho, 1):
                dado_linha = str(input(f'[{num_col}° - Coluna "{coluna}"]: '))
                dados_linha.append(dado_linha)
        
            with open(caminho_arquivo, "a", newline="", encoding="utf-8") as arquivo:
                add_linha = csv.writer(arquivo)
                add_linha.writerow(dados_linha)
        print('Linha(s) adiconada(s) com')
    except Exception as erro:
            print(f'ERRO: {erro.__class__.__name__} : {erro}')
 
def editar_linha_csv(nome_arq):
    """
    Exibe o conteúdo de um arquivo CSV e permite a edição controlada de um campo específico.
    Valida rigorosamente as entradas do usuário (número da linha e nome da coluna) por meio 
    de loops de repetição para evitar quebras por índices ou chaves inválidas.

    Argumentos:
    nome_arq (str): O nome do arquivo a ser editado (sem a extensão .csv).
    """
    nome_arq = nome_arq.strip()
    caminho_arquivo = join(pasta_padrao, f"{nome_arq}.csv")

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            colunas = leitor.fieldnames
            dados_arquivo = list(leitor)
            print('~~~'*20)
            for num_lin, linha in enumerate(dados_arquivo, 1):
                print(f'{num_lin}° linha: {linha}')
            print('~~~'*20)
        while True:
            try:
                numero_linha = int(input('Digite o número da linha que deseja editar: '))
                if 1 <= numero_linha <= len(dados_arquivo):
                    break
                print(f'ERRO: Escolha uma linha entre 1 e {len(dados_arquivo)}')
            except ValueError:
                print('ERRO: Digite um número inteiro válido!')
        print('~~~'*20)
        print(dados_arquivo[numero_linha - 1])
        print('~~~'*20)
        while True:
            nome_coluna = str(input('Digite o nome da coluna que deseja editar: ')).strip()
            if nome_coluna in colunas:
                break
            print(f'ERRO: A coluna "{nome_coluna}" não existe!')
            print(f'Colunas existentes: {colunas}')
        novo_valor = str(input(f'Digite um novo valor para coluna "{nome_coluna}": '))
        dados_arquivo[numero_linha - 1][nome_coluna] = novo_valor   
        with open(caminho_arquivo, "w", newline="", encoding="utf-8") as arquivo:
            reescrever_arquivo = csv.DictWriter(arquivo, fieldnames=colunas)
            reescrever_arquivo.writeheader()
            reescrever_arquivo.writerows(dados_arquivo)
        print('___'*20)
        print('Arquivo alterado com sucesso!')
        print('___'*20)
    except Exception as erro:
        print('xxx'*20)
        print(f'ERRO: {erro.__class__.__name__} : {erro}')
        print('xxx'*20)
        