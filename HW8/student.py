from teacher import ChooseSubject

def StudentFunctions():
    name = input("To see your grades, enter your last name: ")
    operator = -1
    while operator != 0:
        fname = ChooseSubject()
        with open(fname, 'r') as file:
            for line in file:
                list = line.split()
                if name == list[0]: print(name, list[1::])
        operator = int(input("1 - Choose another subject\n \
0 - Exit\n"))