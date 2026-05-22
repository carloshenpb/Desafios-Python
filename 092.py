from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['CTPS'] = int(input('Carteira de trabalho (se não tiver digite 0): '))
if dados['CTPS'] != 0:
    dados['ano_contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposento'] = (dados['ano_contratação'] - nascimento) + 35
print('=-'*20)
for k, v in dados.items():
    print(f'{k.upper()} recebeu o valor: {v}.')