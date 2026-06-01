from math import sin, cos, tan, radians
ang = float(input('Digite um ângulo: '))
cs = cos(radians(ang))
sen = sin(radians(ang))
ta = tan(radians(ang))
print('''O ÂNGULO de {} tem:
 O SENO de {:.2f}
 O COSSENO de {:.2f}
 A TANGENTE de {:.2f}'''.format(ang, sen, cs, ta))