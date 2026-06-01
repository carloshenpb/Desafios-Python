print('[CALCULANDO O IMC DE UMA PESSOA]')

#Captando a altura e o peso da pessoa:
altura = float(input('Qual sua altura? '))
peso = float(input('Qual seu peso em Kilos? '))

#Cálculando o IMC
IMC = peso/altura**2
print(f'Seu IMC é de {IMC:.1f}')

#Status da pessoa:
if IMC < 18.5:
    print('Você está Abaixo do peso! Cuide-se!')
elif IMC <= 25:
    print('Parabéns! Você está no seu peso ideal!')
elif IMC <= 30:
    print('Você está Sobrepeso! Começe a se cuidar!')
elif IMC <= 40:
    print('Você está Obeso! Procure um médico o mais rápido possível!')
else:
    print('PARABÉNS! VOCÊ VAI JOGAR NO VASCO!')
