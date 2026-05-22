print('[FORMANDO TRIÂNGULOS]')

#Captando os lados do triângulos
a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

#Definindo se é possível ou não formar um triângulo e qual o seu tipo:
if a+b>c and a+c>b and b+c>a:
    print('É possível formar um triângulo com essas retas!')
    if a == b and b == c:
        print('O Triângulo formado é Equilátero!')
    elif a != b and b != c and a != c:
        print('O Triângulo formado é Escaleno!')
    elif a == b or b == c or a == c:
        print('O Triângulo formado é Isósceles!')
else:
    print('Infelizmente não é poissível formar um triângulo com essas retas!')