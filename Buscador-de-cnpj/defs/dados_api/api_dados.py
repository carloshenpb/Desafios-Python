import requests

def buscar_cnpj(CNPJ):
    resposta = requests.get(f"https://api.opencnpj.org/{CNPJ}")
    print(resposta.status_code)
    dados = resposta.json()
    return dados

dados_empresa = buscar_cnpj('53868498000175')
print(f'Razão social: {dados_empresa['razao_social']}')
print(f'CNPJ: {dados_empresa['cnpj']}')
print(f'Nome fantasia: {dados_empresa['nome_fantasia']}')
print(f'Natureza Juridica: {dados_empresa['natureza_juridica']}')