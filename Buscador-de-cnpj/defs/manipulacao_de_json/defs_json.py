import json
from os.path import join
from defs.menus.menus import so_opcoes

pasta_padrao = r'C:\Users\carlo\PycharmProjects\Desafios\Buscador-de-cnpj\arquivos'
arquivo_padrao = join(pasta_padrao, f"empresas.json")

def exibir_json_simples():
    """
    Lê o arquivo JSON padrão e exibe no terminal a relação de CNPJs cadastrados
    e suas respectivas estruturas de dados brutas de forma direta e simplificada.
    Utilizado para fins de visualização da organização e aninhamento do arquivo.
    """
    with open(arquivo_padrao, "r", encoding="utf-8") as arquivo:
        empresas = json.load(arquivo)
        for cnpj, dicionario_cnpj in empresas.items():
            print('___'*30)
            print(f'{cnpj} :')
            for dado, valor in dicionario_cnpj.items():
                print(f'{dado} : {valor}')

def exibir_json_tabela():
    """
    Lê o arquivo JSON padrão e exibe os dados das empresas em formato de tabela no terminal.
    Modela colunas alinhadas com larguras fixas para organizar visualmente as informações principais.
    """
    with open(arquivo_padrao, "r", encoding="utf-8") as arquivo:
        empresas = json.load(arquivo)
        print('Empresas cadastradas:')
        print(f'{"CNPJ":<18}|{"Razão Social":<40}|{"Nome Fantasia":<30}|{"Município":<20}|{"UF":<4}|{"Natureza Jurídicia":<30}')
        for cnpj, dicionario_cnpj in empresas.items():
            print('-----'*30)
            razao_social = dicionario_cnpj['razão social'][:40]
            nome_fantasia = dicionario_cnpj['nome fantasia'][:30]
            municipio = dicionario_cnpj['endereço']['municipio'][:20]
            uf = dicionario_cnpj['endereço']['uf'][:4]
            natureza_juridica = dicionario_cnpj['natureza jurídica'][:30]
            print(f'{cnpj:<18}|{razao_social:<40}|{nome_fantasia:<30}|{municipio:<20}|{uf:<4}|{natureza_juridica:<30}')

def filtrar_cnpj_especifico(cnpj):
    cnpj = ''.join(caractere for caractere in str(cnpj) if caractere.isdigit())
    try:
        with open(arquivo_padrao, "r", encoding="utf-8") as arquivo:
            empresas = json.load(arquivo_padrao)
            if not cnpj in empresas.items():
                print('ERRO: Este CNPJ não possuí registro!')
            else:
                for dados in empresas[cnpj].items():
                    print(f'Razão Social: {dados["razão social"]}')
                    print(f'Nome Fantasia: {dados["nome fantasia"]}')
    except Exception as erro:
        print(f'ERRO: {erro.__class__.__name__} : {erro}')