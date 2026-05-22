print('[ Seja Bem vindo ao AprovaCréd! ]')
valor = float(input('Qual valor do Imóvel que você pretende adquirir?   '))
renda = float(input('Qual sua Renda Mensal?  '))
anos = int(input('Em quanto tempo pretende pagar esse empréstimo?'  ))
# A taxa de Juros Anual é de 8%
taxa_anual = 8
# Convertendo a o tempo em meses e calculando a taxa mensal:
meses = anos*12
taxa_mensal = (taxa_anual/100)/12
#Calculando o valor das parcelas mensais:
PMT = (valor*taxa_mensal)/(1-(1+taxa_mensal)**-meses)
#Calculando o Limite que a pessoa pode pagar:
limite = renda*30/100
#Aprovação do empréstimo:
if limite < PMT:
    print('Infelizmente seu empréstimo foi Negado!')
elif limite >= PMT:
    print('Parábens sem empréstimo foi aprovado!')
    print('O Valor da parcela mensal será de {:.2f}'.format(PMT))