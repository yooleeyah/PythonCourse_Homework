intList = list(map(int, input('Введите целые числа в одну строчку через пробел: ').split()))
res = list(filter(lambda x: x > 9 and x < 100, intList))
print(res)