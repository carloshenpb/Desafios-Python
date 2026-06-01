from os.path import exists, join
import csv
from defs.menu.menus import so_opcoes

pasta_padrao = r'C:\Users\carlo\PycharmProjects\Desafios\Manipulação-de-CSV\arquivos'

def verificar_csv(arq_nome):
    """
Verifica se um arquivo CSV já existe em um diretório padrão do sistema.

Argumentos:
    arq_nome (str): O nome do arquivo a ser verificado (sem a extensão .csv).

Retorna:
    bool: Retorna True se o arquivo já existir (bloqueado) 
          ou False se o arquivo não existir (liberado para criação).
"""
    caminho_arquivo = join(pasta_padrao, f'{arq_nome}.csv')
    if exists(caminho_arquivo):
        return True
    else:
        return False
    
def criar_csv(nome_arq, num_col):
    """
Cria um novo arquivo CSV com cabeçalhos personalizados informados pelo usuário,
salvando-o diretamente na pasta padrão configurada globalmente.

Argumentos:
    nome_arq (str): O nome do arquivo a ser criado (sem a extensão .csv).
    num_col (int): A quantidade de colunas que o arquivo terá.
"""

    caminho_arquivo = join(pasta_padrao, f'{nome_arq}')
    cabecalho = []
    for c in range(0, num_col):
        nome_col = str(input(f'Digite o nome da {c+1}° coluna: '))
        cabecalho.append(nome_col)
    
    try:
        with open(caminho_arquivo, "w", newline = "", encoding = "utf-8") as arquivo_novo: 
            criar_arquivo = csv.DictWriter(arquivo_novo, fieldnames = cabecalho)
            criar_arquivo.writeheader()
    except Exception as erro:
        print(f'ERRO: {erro.__class__.__name__}')
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
    #elif modo_exibir == 2:
        #with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
           # leitor = csv.DictReader(arquivo)
