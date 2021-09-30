file = "input.txt"


with open(file) as file_obj:
    lst = []
    i = 0
    for string in file_obj:
        if string == "\n":
            i += len(set(lst))
            lst = []
        else:
            for item in string.rstrip():
                lst.append(item)
    else:
        i += len(set(lst))

print(i)
