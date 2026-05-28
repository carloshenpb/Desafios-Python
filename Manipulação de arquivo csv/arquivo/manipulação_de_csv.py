import csv
from pathlib import Path


def testando_arquivo(arq_nome):
    arq = Path(f"{arq_nome}.csv")
    if arq.exists():
        print(f'{arq_nome}.csv já existe!')
        return True
    else:
        print(f'{arq_nome}.csv não existe!')
        return False

def criar_csv():
    arq_nome = str(input('Digite o nome que deseja que o arquivo tenha: ')).strip()
    num_col = int(input('Digite o número de colunas que deseja: '))
    cabecalho = []
    for c in range(0, num_col):
        nome_col = str(input(f'Digite o nome da {c+1}° coluna: '))
        cabecalho.append(nome_col)
    try:
        with open(f"{arq_nome}.csv", "w", newline="", encoding="utf-8") as arquivo:
            criar = csv.DictWriter(arquivo, fieldnames=cabecalho)
            criar.writeheader()
    except Exception as erro:
        print(f'ERRO: {erro.__class__.__name__}')
    else:
        print(f'{arq_nome}.csv criado com sucesso!')

def adicionar_linha_csv(arq_name):
    contador_linha = 1
    num_linha = int(input('Quantas linhas deseja adicionar? '))
    while contador_linha <= num_linha:
        dados_linha = []
        try:
            with open(f"{arq_name}.csv", "r", encoding="utf-8") as arquivo:
                dados_cabecalho = csv.reader(arquivo)
                cabecalho = next(dados_cabecalho)
            for coluna in cabecalho:
                dado_linha = str(input(f'Digite o que deseja por na coluna {coluna}: '))   
                dados_linha.append(dado_linha)
            with open(f"{arq_name}.csv", "a", newline="", encoding="utf-8") as arquivo:
                add_linha = csv.writer(arquivo)
                add_linha.writerow(dados_linha)
            print('Linha adicionada com sucesso!')
            print('==='*20)
        except Exception as erro:
            print(f'ERRO: {erro.__class__.__name__}')
        contador_linha +=1
  