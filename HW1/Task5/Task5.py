import math
x1 = int(input('Введите x первой координаты: '))
y1 = int(input('Введите y первой координаты: '))
x2 = int(input('Введите x второй координаты: '))
y2 = int(input('Введите y второй координаты: '))
print(round(math.sqrt((x2-x1)**2 + (y2-y1)**2), 4))