i = 0
with open('list.txt') as fileobj:
    for x in fileobj:
        # разбиваем строку за части >>> ['2-6', 'c:', 'fcpwjqhcgtffzlbj']
        list = x.split()

        # разбиваем первый элемент['2-6'] по "-" >>> ['2', '6']
        first_elem_list = list[0].split('-')

        # разбиваем второй элемент['c:'] по ":" >>> ['c', '']
        second_elem_list = list[1].split(':')

        # разбиваем третий ['fcpwjqhcgtffzlbj'] элемент на символы ['f','c','p','w','j','q','h','c','g','t','f','f','z','l','b','j']
        third_elem_list = [c for c in list[2]]
        
        # берем символ с первой нужной позиции['2','6'] (-1 потому что индексы начинаются с 0, а символы в пароле нет)
        letter_in_first_position = third_elem_list[int(first_elem_list[0])-1]

        # берем символ со второй нужной позиции['2','6']
        letter_in_second_position = third_elem_list[int(first_elem_list[1])-1]

        # символ который ищем['c']
        sample_letter = second_elem_list[0]
        
        # элемент может находится только на одной из указанных позиций. Условие: 
        # (символ на первой позиции равен указанному символу И символ на 
        # второй позиции не равен указанному символу) ИЛИ (символ на первой 
        # позиции не равен указанному символу И символ на второй позиции равен 
        # указанному символу)
        if (letter_in_first_position ==sample_letter and letter_in_second_position != sample_letter
            ) or (letter_in_first_position != sample_letter and letter_in_second_position == sample_letter):
            i += 1
print(i)
