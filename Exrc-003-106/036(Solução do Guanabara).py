valor_casa = float(input('Qual o valor da casa? R$'))
salario_mes = float(input('Quanto você ganha por mês? R$'))
anos = int(input('Em quantos anos você pretende pagar por isso? '))

#Calculando a prestação:
prestacao = valor_casa / (anos*12)
print('A prestação será de R${:.2f}'.format(prestacao))

#Decidindo a aprovação do empréstimo:
condicao_para_emprestimo = salario_mes * 30 / 100

if prestacao <= condicao_para_emprestimo:
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO!')