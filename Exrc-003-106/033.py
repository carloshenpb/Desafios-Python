
#n1 = int(input('Digite um número: '))
#n2 = int(input('Digite um número: '))
#n3 = int(input('Digite um número: '))
#print('Os números digitados foram: {}, {}, {}'.format(n1, n2, n3))

#print('O maior número digitado foi: {}'.format(max(n1, n2, n3)))
#print('O menor número digitado foi: {}'.format(min(n1,n2,n3)))

'''Solução do Guanabara'''

a = int(input('Digite um número: '))
b = int(input('Digite um nùmero:'))
c = int(input('Digite um número: '))

menor = a
# Verificando quem é o menor:
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

# Verificando quem é o maior:
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('O menor número digitado é {}'.format(menor))
print('O maior número Digitado foi {}'.format(maior))