file = "input.txt"
i = 1
j = 0
with open(file) as file_obj:
    list = [x for x in file_obj.read()]
    while i != (-1):
        if list[j] == "(":
            i += 1
            j += 1
        elif list[j] == ")":
            i -= 1
            j += 1
    print(j-1)
