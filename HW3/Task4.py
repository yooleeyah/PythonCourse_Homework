number = int(input('Enter number: '))
string = ""
while number != 0:
    string = str((number % 2)) + string
    number //= 2
print(string)