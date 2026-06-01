def escreva(msg):
    tam = len(msg)+4
    print('~'*tam)
    print(f'  {msg.upper()}')
    print('~'*tam)

# Programa principal
frase = str(input('Digite uma frase: '))
escreva(frase)
