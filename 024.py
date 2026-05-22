# cid = str(input('Qual o nome da sua cidade? ')).strip()
# C = cid.upper()
# print('{}'.format('SANTO' in C))

'''Solução do professor Guanabara!'''

cid = str(input('Qual nome da sua cidade? ')).strip()
print(cid[:5].upper() == 'SANTO')