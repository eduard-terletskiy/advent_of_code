file = "input.txt"


def square(str):
    l, w, h = str[0], str[1], str[2]
    return (2*l)+(2*w)+(l*w*h)


squar = 0
with open(file) as file_obj:
    for x in file_obj:
        str = x.strip().split('x')
        str = [int(item) for item in str]
        str.sort()
        squar += square(str)
print(squar)
