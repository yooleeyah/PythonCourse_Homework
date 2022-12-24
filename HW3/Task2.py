list = [2, 3, 4, 5, 6]
for i in range(len(list)):
    if i > (len(list) - 1 - i): break
    print(list[i] * list[len(list)-1-i], end = " ")