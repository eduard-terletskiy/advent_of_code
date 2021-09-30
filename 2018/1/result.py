file = 'input.txt'
res = 0
with open( file ) as file_obj:
    for x in file_obj:
            res=res + int(x)
    print(res)
        