'''from math import pow, sqrt
cat = float(input('Comprimento do cateto oposto:  '))
adj = float(input('Comprimento do cateto adjacente:  '))
hpo = sqrt(pow(cat, 2) + pow(adj, 2))
print('A hipotenusa é {:.2f}'.format(hpo))'''

from math import hypot
cat = float(input('Comprimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente: '))
hpo = hypot(cat, adj)
print('A hipotenusa é {:.2f}'.format(hpo))