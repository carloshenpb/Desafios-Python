sla = float(input('Qual o seu salário? '))

if sla > 1250:
    amnt = sla + (sla*10/100)
    print('O salário de {:.2f}R$ com o aumento de 10% passará a ser de {:.2f}R$'.format(sla, amnt))
    print('O valor do aumento é de {:.2f}R$'.format(amnt - sla))
else:
    amnt = sla + (sla*15/100)
    print('O salário de {:.2f}R$ com o aumento de 15% passará a ser de {:.2f}R$'.format(sla, amnt))
    print('O valor do aumento é de {:.2f}R$'.format(amnt - sla))
