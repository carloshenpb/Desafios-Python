import requests
from os.path import join
import json

pasta_padrao = r'C:\Users\carlo\PycharmProjects\Desafios\Buscador-de-cnpj\arquivos'
arquivo_padrao = join(pasta_padrao, f"empresas.json")

def buscar_cnpj(cnpj):
    try:
        requisicao = requests.get(f"https://api.opencnpj.org/{cnpj}", timeout=7)
        requisicao.raise_for_status()
        dados_api = requisicao.json()
        return dados_api
    except requests.exceptions.ConnectionError:
        print('ERRO: Sem conexão com a internet!')
        return None
    except requests.exceptions.Timeout:
        print('ERRO: A requisição demorou tempo demais!')
        return None
    except requests.exceptions.HTTPError as errohttp:
        if errohttp.response.status_code in (400, 404):
            print('ERRO: CNPJ inválido ou não encontrado!')
        else:
            print(f'ERRO: {errohttp.__class__.__name__} : {errohttp}')
        return None

def adicionar_cnpj(cnpj):
    dados_cnpj = buscar_cnpj(cnpj)
    if not dados_cnpj:
        return
    
    try:
        try:
            with open(arquivo_padrao, "r", encoding="utf-8") as arquivo:
                dados_empresas = json.load(arquivo)
        except(FileNotFoundError, json.JSONDecodeError):
            dados_empresas = {}

        lista_de_telefones = []
        for telefone in dados_cnpj['telefones']:
            dados_telefone = {
                "ddd": telefone["ddd"],
                "número_telefone": telefone["numero"]
            }
            lista_de_telefones.append(dados_telefone)

        cnpj_empresa = dados_cnpj.get("cnpj")

        dados_empresas[cnpj_empresa] = {
        "nome fantasia": dados_cnpj.get("nome_fantasia"),
        "razão social": dados_cnpj.get("razao_social"),
        "cnpj": dados_cnpj.get("cnpj"),
        "natureza jurídica": dados_cnpj.get("natureza_juridica"),
        "endereço":{
            "tipo logradouro": dados_cnpj.get("tipo_logradouro"),
            "logradouro": dados_cnpj.get("logradouro"),
            "número da residência": dados_cnpj.get("numero"),
            "complemento": dados_cnpj.get("complemento"),
            "bairro": dados_cnpj.get("bairro"),
            "municipio": dados_cnpj.get("municipio"),
            "uf": dados_cnpj.get("uf")
        },
        "contatos":{
            "e-mail": dados_cnpj.get("email"),
        "telefones": lista_de_telefones
        }
        }
        
        with open(arquivo_padrao, "w", encoding="utf-8") as arquivo:
            json.dump(dados_empresas,
                       arquivo,
                       ensure_ascii=False,
                       indent=4
                       )
        print('Dados adicionados com sucesso!')
    except Exception as erro:
        print(f'ERRO: {erro.__class__.__name__} : {erro}')

