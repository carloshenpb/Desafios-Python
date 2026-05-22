def linha():
     return '-=-'*30
def voto(ano_nascimento):
    """Função responsavel por calcular a idade do usuário com base no ano do seu nascimento
    e retornar a obrigatoriedade do voto.
    - ano_nascimento = ano de nascimento do user"""
    from datetime import datetime

    idade = datetime.now().year - ano_nascimento
    if 18 <= idade <= 70:
        return f'Com {idade} anos o voto é OBRIGATÓRIO!'
    elif idade < 16:
        return f'Com {idade} anos o voto é NEGADO!'
    else:
        return f'Com {idade} anos o voto é FACULTATIVO!'

# Programa Principal
nascimento = int(input('Digite seu ano de nascimento: '))
linha()
print(voto(nascimento))
linha()
help(voto)