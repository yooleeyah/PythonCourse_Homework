data = [12,'sadf',5643]
print(list(filter(lambda x: type(x) == str, data)))
print(list(filter(lambda x: type(x) == int, data)))