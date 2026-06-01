#vel = int(input('Qual a velocidade do carro? '))
#limite = 80
#multa = 0

#if vel <= limite:
    #print('O carro está em uma velocidade dentro do limite!')
#else:
   # multa = (vel-limite)*7
    #print('O carro ultrapassou a velocidade permitida! Será aplicada uma multa de {}R$'.format(multa))

'''Solução do Guanabara:'''

velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite de velocidade!')
    multa = (velocidade - 80)*7
    print('O valor da multa é de {:.2}R$'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')