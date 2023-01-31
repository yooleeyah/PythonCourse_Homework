from teacher import TeacherFunctions
from student import StudentFunctions

def Identification():
    id = int(input("If you are a teacher, enter 1,\n \
if you are a student, enter 2\n"))
    if id == 1: TeacherFunctions()
    if id == 2: StudentFunctions()