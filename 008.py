metros = float(input('Digite uma medida em metros:  '))
km = metros/1000
hm = metros/100
dam = metros/10
dm = metros*10
cm= metros*100
mm= metros*1000
print('A medida de {} metros corresponde a:\n{:.3f} quilômetros\n{:.2f} hectômetros\n{:.2f} decametros'.format(metros, km, hm, dam))
print('{} decimetros \n{} centimetros \n{} milimetros '.format(dm, cm, mm))