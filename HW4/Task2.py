number = int(input('Enter N: '))
i = 2
while number != 1:
    if number % i == 0: 
        print(i, end = ' * ')
        number /= i
    else: i +=1