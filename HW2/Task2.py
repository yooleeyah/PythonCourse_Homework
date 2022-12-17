number = int(input('Enter n: '))
for i in range(2, number + 1):
    if number % i == 0: break
print(i)