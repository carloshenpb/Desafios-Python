def linha(tam = 20):
    """Função para exibir uma linha
    :param tam: ( Opicional ) Tamanho da linha."""
    print('_'* tam)

def simounao(msg, msg2=''):
    """Função para definir a continuação ou não do programa principal."""
    while True:
        resposta = str(input(msg)).strip().upper()
        if resposta == 'S':
            return True
        elif resposta == 'N':
            if msg2:
                linha(40)
                print(f'{msg2:^40}')
                linha(40)
            else:
                linha(40)
            return False
        else:
            print('Resposta Invalida! Digite apenas S ou N!')

def notas(*nota, sit = False):
    """- Função para analisar várias notas e definir a situação de uma turma
       :param nota: Paraâmetro que armazena várias notas de alunos
       :param sit: Mostra a sitação da turma. Boa > 8; 7 >= Mediana >=6 ; Ruim < 6
       :return dicturma: Retorna um dicionário com as informações da turma"""
    dicturma = dict()
    dicturma['Quantidade de notas'] = len(nota)
    dicturma['Maior nota'] = max(nota)
    dicturma['Menor nota'] = min(nota)
    dicturma['Média'] = sum(nota)/ len(nota)
    if sit:
        if dicturma['Média'] > 8:
            dicturma['Situação'] = 'Boa'
        elif 7 >= dicturma['Média'] >= 6:
            dicturma['Situação'] = 'Moderada'
        else:
            dicturma['Situação'] = 'Ruim'
    return dicturma

# Programa principal
linha(40)
print(notas(3.5, 5, 7.8, 9, 1.5, sit=True))
linha(40)
help(notas)