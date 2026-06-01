from os.path import exists, join

def verificar_csv(arq_nome):
    pasta_padrao = r'C:\Users\carlo\PycharmProjects\Desafios\Manipulação-de-CSV\arquivos'
    caminho_arquivo = join(pasta_padrao, f'{arq_nome}.csv')
    if exists(caminho_arquivo):
        print(f'ERRO: O arquivo "{arq_nome}.csv" já existe!')
        return False
    else:
        return True