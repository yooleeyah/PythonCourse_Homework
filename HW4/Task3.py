str = input('Введите последовательность чисел: ')
list = [int(x) for x in str.split()]
for i in list:
    if list.count(i) == 1: print(i, end = ' ')