b = float(input('Digite a largura da Parede:  '))
h = float(input('Digite a altura da Parede:  '))
area = b*h
tinta = area/2
print('''Sua parede tem as dimensões {}X{}.
A área da sua parede é de {}m^2
Para pintar essa parede, você deverá utliziar {:.3f}L de tinta'''.format(b, h, area, tinta))