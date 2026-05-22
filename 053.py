'''frase = str(input('Digite uma frase:  '))
frase_sem_espaços = frase.replace(' ', '').upper()
palindromo = frase_sem_espaços[::-1]

# Verificando se a frase é ou não um palíndromo
print(f'O inverso da frase digitada é: {palindromo}')
if frase_sem_espaços == palindromo:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')'''

# Solução do Guanabara

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(f' A frase invertida fica assim: {inverso}')
if inverso == junto:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')