import math
fuel = 'input.txt'

# -------------------------------------------------
# part one:
# result = 0
# with open(fuel) as fl_obj:
#     for res in fl_obj:
#         res = math.floor(int(res)/3) - 2
#         result = result + res
#     print(result)
# part one end
# -------------------------------------------------
#

# -------------------------------------------------
# part two:
a = 0
with open(fuel) as fl_obj:
    for res in fl_obj:
        result = 0
        while int(res) > 0:
            res = math.floor(int(res)/3) - 2
            if res > 0:
                result = result + res
        a += result
    print(a)

