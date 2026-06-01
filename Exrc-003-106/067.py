while True:
    num = int(input('De qual número você deseja saber a tabuada? '))
    if num < 0:
        break
    else:
        print('_' * 20)
        for c in range(1, 11):
            print(f'{num} X {c} = {num * c}')
        print('_' * 20)
print('FIM')