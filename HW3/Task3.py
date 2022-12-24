list = [1.1, 1.2, 3.1, 5, 10.01]
for i in range(len(list)):
    list[i] = round(list[i] % 1, 2)
for i in list:
    if i == 0: list.remove(i)
# print(list)
print(max(list) - min(list))