import random
k = int(input('Задайте натуральную степень k: '))
for i in range(k+1):
    if k == 1: print(f'{random.randint(0,100)}x + ', end = '')
    elif k == 0: print(f'{random.randint(0,100)}')
    else: print(f'{random.randint(0,100)}x^{k} + ', end = '')
    k -= 1