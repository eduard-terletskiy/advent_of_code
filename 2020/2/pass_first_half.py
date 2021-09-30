# a <= list.count(c) <= b
# a   b  c     list
# |   |  |      |
# 2 - 6  c : fcpwjqhcgtffzlbj

i = 0
with open('list.txt') as fileobj:
    for x in fileobj:
        # разбиваем строку за части >>> ['2-6', 'c:', 'fcpwjqhcgtffzlbj']
        list = x.split()

        # разбиваем первый элемент['2-6'] по "-" >>> ['2', '6']
        first_elem_list = list[0].split('-')

        # разбиваем второй элемент['c:'] по ":" >>> ['c', '']
        second_elem_list = list[1].split(':')

        # считаем количество вхождений first_elem_list[0](c) в list[2](fcpwjqhcgtffzlbj) >>> 2
        numb = list[2].count(second_elem_list[0])

        # проверяем входит ли полученное число в диапазон(от 2 до 6) первое число - first_elem_list[0](2), второе число - first_elem_list[1](6)
        if int(first_elem_list[0]) <= int(numb) <= int(first_elem_list[1]):
            i += 1
print(i)
