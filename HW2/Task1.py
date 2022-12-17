number = int(input('Enter n: '))
mult = 1
for i in range(number): 
    mult *= number
    number -= 1
print(mult)