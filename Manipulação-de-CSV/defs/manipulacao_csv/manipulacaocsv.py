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
    caminho_arquivo = join(pasta_padrao, f'{nome_arq}.csv')

    como_exibir = ('EXBIÇÃO SIMPLES', 'EXIBIÇÃO COM DICTREADER')
    modo_exibir = so_opcoes(como_exibir)

    if modo_exibir == 1:
        with open(caminho_arquivo, "r", encoding = "utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                print(linha)
    elif modo_exibir == 2:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
