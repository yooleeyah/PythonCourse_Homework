number = int(input('Enter n: '))
# list = [0] * (number*2 + 1)
list = [i for i in range(-number, number + 1)]
print(list)
indexList = [2,2,3,1,8]
mult = 1
i = 0
for i in indexList: 
    mult *= list[i]
print(mult)