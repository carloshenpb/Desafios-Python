from os.path import exists, join

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
    
