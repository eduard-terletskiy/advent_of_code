i = 0
num = 0
with open('input.txt') as f:
    file = f.readlines()
    # for st in range(0, 11, 1): для 1-4 строк
    for st in range(0, 323, 2):
        print(st)
        print(file[st])
        a = len(file[st])
        third_elem_list = [c for c in file[st]]
        
        if num > (a - 2):
            num = num - (a-1)
        if third_elem_list[num] == '#':
            i += 1
        num += 1
print(i)
