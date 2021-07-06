list = "list.txt"

with open(list) as fileobj:
    a = fileobj.readlines()
    list = []
    for x in a:
        for t in a:
            b = int(t) + int(x)
            if b == 2020:
                y = int(t) * int(x)
                list.append(y)
print(list)
