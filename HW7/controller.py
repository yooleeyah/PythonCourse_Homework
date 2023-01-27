from models import AddContact, ShowBook

def Dialog():
    operator = -1
    while operator != 0:
        print("Choose an operation:\n \
                1 - Add contact to phone book\n \
                2 - Show phone book\n \
                0 - End programm\n")
        operator = int(input())
        if operator == 1: AddContact()
        if operator == 2: ShowBook()