#nome = str(input('Digite seu nome: ')).strip()
#partes = nome.split()

#p1 = partes[0]
#pu = partes[-1]

#print('Seu primeiro nome é {}.'.format(p1))
#print('Seu ultimo nome é {}.'.format(pu))

'''Solução do professor Guanabara!'''

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
