from datetime import date
#captando o ano de nascimento da pessoa
ano_nascimento = int(input('Qual seu ano de nascimento? '))
ano_atual = date.today().year

#calculando a idade atual da pessoa
idade_atual = ano_atual - ano_nascimento
idade_alistamento = 18

if idade_atual < idade_alistamento:
    print(f'Ainda não está na hora! Faltam {idade_alistamento - idade_atual} anos para você se alistar!')
elif idade_atual == idade_alistamento:
    print('Você já tem 18 anos, está na hora de se alistar! Faça seu alistamento no site: www.alistamentoexercitobr.com')
else:
    print(f'Você passou do prazo do alistamento! Era para você ter se alistado a {idade_atual-idade_alistamento} anos atrás!')
