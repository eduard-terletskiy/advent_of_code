file = "input.txt"


def square(str, m):
    l, w, h = str[0], str[1], str[2]
    return (2*l*w)+(2*w*h)+(2*h*l)+m


squar = 0
with open(file) as file_obj:
    for x in file_obj:
        str = x.strip().split('x')
        str = [int(item) for item in str]
        minimal = min([str[0]*str[1], str[1]*str[2], str[0]*str[2]])
        squar += square(str, minimal)
print(squar)
