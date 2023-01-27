def AddContact():
    surname = input("Enter last name: ")
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    comment = input("Enter description: ")
    with open('phoneBook.txt', 'a') as file:
        file.write(f'Last name: {surname}\nName: {name}\nPhone number: {number}\nDescription: {comment}\n\n')
    with open('phoneBook.csv', 'a') as file2:
        file2.write(f'{surname};{name};{number};{comment}\n')

def ShowBook():
    with open('phoneBook.txt', 'r') as file:
        data = file.read()
        print(data)
    # with open('phoneBook.csv', 'r') as file2:
    #     data2 = file2.read()
    #     print(data2)
