def Coding(string):
    symbol = string[0]
    count = 0
    result = ""
    for i in string:
        if i == symbol: count += 1
        else:
            result += str(count) + symbol
            symbol = i
            count = 1
    result += str(count) + symbol
    return result

def Decoding(string):
    result = ""
    num = ""
    for i in string:
        if i.isdigit(): num += i
        else: 
            for j in range(int(num)): result += i
            num = ""
    return result


data = open('file3.txt', 'r')
for line in data: string = line
data.close()
string2 = Coding(string)
print(string2)
print(Decoding(string2))