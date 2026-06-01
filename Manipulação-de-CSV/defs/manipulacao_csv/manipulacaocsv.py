from os.path import exists, join
import csv

def verificar_csv(arq_nome):
    """
Verifica se um arquivo CSV já existe em um diretório padrão do sistema.

Argumentos:
    arq_nome (str): O nome do arquivo a ser verificado (sem a extensão .csv).

Retorna:
    bool: Retorna False se o arquivo já existir (bloqueado) 
          ou True se o arquivo não existir (liberado para criação).
"""
    pasta_padrao = r'C:\Users\carlo\PycharmProjects\Desafios\Manipulação-de-CSV\arquivos'
    caminho_arquivo = join(pasta_padrao, f'{arq_nome}.csv')
    if exists(caminho_arquivo):
        print(f'ERRO: O arquivo "{arq_nome}.csv" já existe!')
        return False
    else:
        return True
    
def criar_csv(nome_arq, num_col):
    cabecalho = []
    for c in range(0, num_col):
        nome_col = str(input(f'Digite o nome da {c+1}° coluna: '))
        cabecalho.append(nome_col)
    
    try:
        with open(f"{nome_arq}.csv", "w", newline = "", encoding = "utf-8") as arquivo_novo: 
            criar_arquivo = csv.DictWriter(arquivo_novo, fieldnames = cabecalho)
            criar_arquivo.writeheader()
    except Exception as erro:
        print(f'ERRO: {erro.__class__.__name__}')
    else:
        print('Arquivo criado com sucesso!')