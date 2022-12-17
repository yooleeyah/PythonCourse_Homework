number = int(input('Enter n: '))
sum = 0
for i in range(0, number + 1, 2):
    sum += i
    i += 2
print(sum)