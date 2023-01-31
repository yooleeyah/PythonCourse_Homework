def TeacherFunctions():
    operator = -1
    while operator != 0:
        print("Choose an operation:\n \
1 - Enter student's grades\n \
0 - Exit")
        operator = int(input())
        if operator == 1: EnterGrade()

def ChooseSubject():
    print("Choose a subject:\n \
            1 - Biology\n \
            2 - English\n \
            3 - Geography\n \
            4 - Mathematics")
    subj = int(input())
    if subj == 1: fileName = "Biology.txt"
    if subj == 2: fileName = "English.txt"
    if subj == 3: fileName = "Geography.txt"
    if subj == 4: fileName = "Mathematics.txt"
    return fileName

def EnterGrade():
    fname = ChooseSubject()
    name = input("Enter student's last name: ")
    grades = input("Enter grades: ")
    with open(fname, 'a+') as file:
        for line in file:
            list = line.split()
            if name == list[0]: 
                string = line + grades
            file.write(string)
        else: 
            string = name + " " + grades
        file.write(string + '\n')