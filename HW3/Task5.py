number = int(input('Enter number: '))
list = [0, 1]
for i in range(number - 1): list.append(list[i] + list[i+1])
for i in range(number): list.insert(0, list[1] - list[0])
print(list)