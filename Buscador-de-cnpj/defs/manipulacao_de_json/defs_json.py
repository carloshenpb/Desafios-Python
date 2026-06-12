import json
from os.path import join

pasta_padrao = r'C:\Users\carlo\PycharmProjects\Desafios\Buscador-de-cnpj\arquivos'
arquivo_padrao = join(pasta_padrao, f"empresas.json")

def exibir_json_simples():
    with open(arquivo_padrao, "r", encoding="utf-8") as arquivo:
        empresas = json.load(arquivo)
        for cnpj, dicionario_cnpj in empresas.items():
            print('___'*30)
            print(f'{cnpj} :')
            for dado, valor in dicionario_cnpj.items():
                print(f'{dado} : {valor}')

def exibir_json_tabela():
    with open(arquivo_padrao, "r", encoding="utf-8") as arquivo:
        empresas = json.load(arquivo)
        print('Empresas cadastradas:')
        print(f'{"CNPJ":<18}|{"Razão Social":<40}|{"Nome Fantasia":<30}|{"Município":<20}|{"UF":<4}|{"Natureza Jurídicia":<30}')
        for cnpj, dicionario_cnpj in empresas.items():
            print('-----'*30)
            razao_social = dicionario_cnpj['razão social']
            nome_fantasia = dicionario_cnpj['nome fantasia']
            municipio = dicionario_cnpj['endereço']['municipio']
            uf = dicionario_cnpj['endereço']['uf']
            natureza_juridica = dicionario_cnpj['natureza jurídica']
            print(f'{cnpj:<18}|{razao_social:<40}|{nome_fantasia:<30}|{municipio:<20}|{uf:<4}|{natureza_juridica:<30}')
            