import math
x1, y1 = int(input('Введите координаты первой точки через Enter: ')), int(input())
x2, y2 = int(input('Введите координаты второй точки через Enter: ')), int(input())
print(round(math.sqrt((x2-x1)**2 + (y2-y1)**2), 4))