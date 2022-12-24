list = [2, 3, 5, 9, 3]
sum = 0
for i in range(1,len(list)):
    if i % 2 != 0: sum += list[i]
print(sum)