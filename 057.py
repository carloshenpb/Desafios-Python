'''# Inicio: Primeira pergunta! Macho[M] ou Femea [F]?
sexo = str(input('Qual seu sexo? [M / F]: ')).upper().strip()[0]

 # Iniciando o laço
while sexo != 'M' and sexo != 'F':
     print('ERRO! VALOR DIGITADO É INVALIDO! TENTE NOVAMENTE!')
     sexo = str(input('Qual seu sexo? [M / F]: ')).upper().strip()[0]
 # Condições de parada
if sexo == 'M':
         print('Sexo Masculino registrado!')
elif sexo == 'F':
         print('Sexo Feminino registrado!')

print('FIM')'''

# Solução do Guanabara:
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo= str(input('ERRO! Dado inválido! Por favor, informe seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
