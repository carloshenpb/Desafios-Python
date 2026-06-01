exprs = str(input('Digite sua expressão: '))
pilha = []
for simbl in exprs:
    if simbl == '(':
        pilha.append('(')
    elif simbl == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')

if len(pilha) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')