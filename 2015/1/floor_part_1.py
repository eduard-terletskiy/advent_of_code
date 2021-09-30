file = "input.txt"

with open(file) as file_obj:
    list = file_obj.readlines()
    left_parenthesi = "".join(list).count('(')
    right_parenthesi = "".join(list).count(')')

    print(left_parenthesi-right_parenthesi)
