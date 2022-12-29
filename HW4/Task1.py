import math
number = int(input('Введите число знаков после запятой: '))
coeff = 0.1**number
pi = int(math.pi // coeff)
print(pi/10**number)