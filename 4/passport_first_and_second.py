from os import terminal_size
import re
from typing import Pattern
passports = 'input.txt'
dict_passport = {}
list_passport = []
collections = ["iyr", "byr", "eyr", "hgt", "hcl", "ecl", "pid"]


def byr(x):
    if 1920 <= int(x) <= 2002:
        return True


def iyr(x):
    if 2010 <= int(x) <= 2020:
        return True


def eyr(x):
    if 2020 <= int(x) <= 2030:
        return True


def hgt(x):
    pattern = r'^([0-9]{3}?[cm])'
    pattern_1 = r'^([0-9]{2}?[in])'
    if re.match(pattern, x):
        res = re.findall(r'^([0-9]{3}?)', x)
        if 150 <= int(res[0]) <= 193:
            return True
    elif re.match(pattern_1, x):
        res = re.findall(r'^([0-9]{2}?)', x)
        if 59 <= int(res[0]) <= 76:
            return True


def ecl(x):
    ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if x in ecl:
        return True


def hcl(x):
    pattern = r'^([#]{1}[0-9a-f]{6}?$)'
    if re.match(pattern, x):
        return True


def pid(x):
    pattern = r'^([0-9]{9}?$)'
    if re.match(pattern, x):
        return True


def checking_condition(x):
    if (byr(x['byr']) and
        iyr(x['iyr']) and
        eyr(x['eyr']) and
        hgt(x['hgt']) and
        hcl(x['hcl']) and
        ecl(x['ecl']) and
        pid(x['pid'])):
            return True

with open(passports) as file_obj:
    try:
        for passport in file_obj:
            if passport == "\n":
                list_passport.append(dict_passport.copy())
                dict_passport.clear()
            else:
                list_item_passport = passport.split()
                for item in list_item_passport:
                    item = item.split(':')
                    dict_passport[item[0]] = item[1]
    except:
        print("Exeption")
    finally:
        list_passport.append(dict_passport.copy())
i = 0
collections = ["iyr", "byr", "eyr", "hgt", "hcl", "ecl", "pid"]
for x in list_passport:
    if set(collections).issubset(x):
        # if checking_condition(x): uncomment for part two
            i += 1    
print(i)
