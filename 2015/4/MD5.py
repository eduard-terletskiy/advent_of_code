import hashlib
import re

i = -1

while True:
    i+=1
    md5 = hashlib.md5('iwrupvqb{}'.format(i).encode('utf-8')).hexdigest()
    print(' \n '+md5)
    # if re.match(r'00000', md5): for part 1
    if re.match(r'000000', md5):
        print(i)
        break