from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('=-'*20)
    print(f'Contador de {inicio} até {fim} de {passo} em {passo}:')
    sleep(2.5)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += passo
        print('FIM')
    if inicio > fim:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= passo
        print('FIM')

#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é a sua vez! Faça do seu jeito:')
i = int(input('Digite o incio:'))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
contador(inicio=i, fim=f, passo=p)