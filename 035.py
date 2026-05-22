a = float(input('Digite o comprimento da  primeira reta: '))
b = float(input('Digite o comprimento da  segunda reta: '))
c = float(input('Digite o compriemnto da terceira reta: '))

if a+b>c and a+c>b and b+c>a:
    print('É possível formar um triângulo com essas retas!')
else:
    print('Infelizmente não é possível formar um triângulo com essas retas!')