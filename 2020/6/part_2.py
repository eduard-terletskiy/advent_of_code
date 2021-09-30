file = "site.txt"


with open(file) as file_obj:
    lst = []
    i = 0
    for string in file_obj:
        if string == "\n":
            dups = [x for x in lst if lst.count(x) > 1]
            if len(dups) == 0:
                i += len(set(lst))
                lst = []
            else:
                i += len(set(dups))
                lst = []
        else:
            for item in string.rstrip():
                lst.append(item)
print(i)
