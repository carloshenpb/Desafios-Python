# nome = str(input('Digite seu nome completo: '))
# M = nome.upper()
# m = nome.lower()
# letras = len(nome.replace(" ", ""))
# prim_nome = nome.split()[0]
# print('O nome em letras Maiúsculas fica assim: {}'.format(M))
# print('O nome em letras minúsculas fica assim: {}'.format(m))
# print('O nome tem {} letras.'.format(letras))
# print('O primeiro nome é: {}'.format(prim_nome)) #Era pra contar quantas letras tem o primeiro nome!!



#Resolução de acordo com o professor Guanabara:
nome = str(input('Digite seu nome: ')).strip() #O .strip é utilizado para remover os espaços antes e após os caracteres da string!
print('Analisando seu nome....')
print('Seu nome em letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas: {}'.format(nome.lower()))
print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))