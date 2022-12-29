polynomial1 = open('file1.txt', 'r')
str1 = polynomial1.readline()
polynomial1.close
polynomial2 = open('file2.txt', 'r')
str2 = polynomial2.readline()
polynomial2.close
list1 = [x for x in str1.split()]
list2 = [x for x in str2.split()]
for i in list1:
    if i == '+': list1.remove(i)
for i in list2:
    if i == '+': list2.remove(i)
print(list1)
print(list2)