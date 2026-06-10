import requests

resposta = requests.get("https://brasilapi.com.br/api/cnpj/v1/{cnpj}")
print(resposta.status_code)

