#-------------------------------------------------------------------------------
# Name:        Logic Selector f(ABCDEF)
# Purpose:
#
# Author:      Sehktel
#
# Created:     02.02.2024
# Copyright:   (c) TH-code 2024
# Licence:     MIT
#-------------------------------------------------------------------------------

import array as arr
import random
from itertools import permutations
from itertools import combinations
from collections import Counter


rows, cols = (64, 7)
lut = [[0]*cols for _ in range(rows)]
results = set()

def init_lut():
    nums = [[0]*cols]*rows

    for i in range(64):
        F = (i >> 0) & int('00000001', 2)
        E = (i >> 1) & int('00000001', 2)
        D = (i >> 2) & int('00000001', 2)
        C = (i >> 3) & int('00000001', 2)
        B = (i >> 4) & int('00000001', 2)
        A = (i >> 5) & int('00000001', 2)
        # print(A,B,C,D,E,F)
        nums[i] = [A, B, C, D, E, F, random.randint(0, 1)]

        print(nums[i])
    return nums
        # pass

def generate_gray_code(n):
    if n <= 0:
        return []

    gray_code = ['0', '1']

    for i in range(2, 1 << n):
        print (i)
        for j in range(len(gray_code) - 1, -1, -1):
            gray_code.append(gray_code[j])

        for j in range(len(gray_code) // 2):
            gray_code[j] = '0' + gray_code[j]
        for j in range(len(gray_code) // 2, len(gray_code)):
            gray_code[j] = '1' + gray_code[j]

    return gray_code


def find_mask(sequence):
    length = len(sequence[0])
    common_mask = ""
    for i in range(length):
        if all(s[i] == sequence[0][i] or s[i] == "x" for s in sequence):
            common_mask += sequence[0][i]
        else:
            common_mask += "x"

    return common_mask

def get_n (n):
    global lut
    print( bin(n)[2:].zfill(6), "{:2d}".format(n), end='  : ')
    for i in range(6):
        mask = 1 << i
        p =  n ^ mask
        if lut[n][6] == lut[p][6]:
            print(lut[p][0:6], "{:2d}".format(p), end=' ')
    print()

def get_n1 (n):
    global lut
    global results
    flag = False
##    print( bin(n)[2:].zfill(6), "{:2d}".format(n), end='  : \n')
##    print ( bin(n)[2:].zfill(6)[:3], bin(n)[2:].zfill(6)[3:], '  |  ',
##            bin(0)[2:].zfill(6)[:3], bin(0)[2:].zfill(6)[3:], '  |  ',
##            bin(n)[2:].zfill(6)[:3], bin(n)[2:].zfill(6)[3:], '  |  ',
##            lut[n][6])

    input_sequence=set()
    s = '{}{}{}{}{}{}'.format(lut[n][0],lut[n][1],lut[n][2],lut[n][3],lut[n][4],lut[n][5])
    input_sequence.add(s)

    for i in range(6):
        mask = 1 << i
        p =  n ^ mask
        if lut[n][6] == lut[p][6]:
            s = '{}{}{}{}{}{}'.format(lut[p][0],lut[p][1],lut[p][2],lut[p][3],lut[p][4],lut[p][5])
            input_sequence.add(s)
##                print (bin(n)[2:].zfill(6)[:3],     bin(n)[2:].zfill(6)[3:], '  |  ',
##                       bin(mask1)[2:].zfill(6)[:3], bin(mask1)[2:].zfill(6)[3:], '  |  ',
##                       bin(p)[2:].zfill(6)[:3],     bin(p)[2:].zfill(6)[3:], '  |  ',
##                       lut[n][6] == lut[p][6])

    all_combinations = set(combinations(input_sequence, 2))
##    print(input_sequence)
    for combination in all_combinations:
        result = find_mask(combination)
        if (result.count('x') == 1):
            results.add(result)
            flag = True
            #print(combination, end=' -- ')
            #print(result)
    return flag
#    print()
##    for result in results:
##        print(result)


def get_n2 (n):
    global lut
    global results
    flag = False

##    print( bin(n)[2:].zfill(6), "{:2d}".format(n), end='  : \n')
##    print ( bin(n)[2:].zfill(6)[:3], bin(n)[2:].zfill(6)[3:], '  |  ',
##            bin(0)[2:].zfill(6)[:3], bin(0)[2:].zfill(6)[3:], '  |  ',
##            bin(n)[2:].zfill(6)[:3], bin(n)[2:].zfill(6)[3:], '  |  ',
##            lut[n][6])

    input_sequence=set()
    s = '{}{}{}{}{}{}'.format(lut[n][0],lut[n][1],lut[n][2],lut[n][3],lut[n][4],lut[n][5])
    input_sequence.add(s)

    for i in range(6):
        mask = 1 << i
        for j in range(i, 6):
            mask1 = mask | (1 << j)
            p =  n ^ mask1
            if lut[n][6] == lut[p][6]:
                s = '{}{}{}{}{}{}'.format(lut[p][0],lut[p][1],lut[p][2],lut[p][3],lut[p][4],lut[p][5])
                input_sequence.add(s)
##                print (bin(n)[2:].zfill(6)[:3],     bin(n)[2:].zfill(6)[3:], '  |  ',
##                       bin(mask1)[2:].zfill(6)[:3], bin(mask1)[2:].zfill(6)[3:], '  |  ',
##                       bin(p)[2:].zfill(6)[:3],     bin(p)[2:].zfill(6)[3:], '  |  ',
##                       lut[n][6] == lut[p][6])

    all_combinations = set(combinations(input_sequence, 4))
##    print(input_sequence)
    for combination in all_combinations:
        result = find_mask(combination)
        if (result.count('x') == 2):
            results.add(result)
            flag = True
            #print(combination, end=' -- ')
            #print(result)
    return flag

#    print()
##    for result in results:
##        print(result)




def get_n3 (n):
    global lut
    global results
    flag = False
##    print( bin(n)[2:].zfill(6), "{:2d}".format(n), end='  : \n')
##    print ( bin(n)[2:].zfill(6)[:3], bin(n)[2:].zfill(6)[3:], '  |  ',
##            bin(0)[2:].zfill(6)[:3], bin(0)[2:].zfill(6)[3:], '  |  ',
##            bin(n)[2:].zfill(6)[:3], bin(n)[2:].zfill(6)[3:], '  |  ',
##            lut[n][6])

    input_sequence=set()
    s = '{}{}{}{}{}{}'.format(lut[n][0],lut[n][1],lut[n][2],lut[n][3],lut[n][4],lut[n][5])
    input_sequence.add(s)

    for i in range(6):
        mask = 1 << i
        for j in range(i, 6):
            mask1 = mask | (1 << j)
            for k in range (j, 6):
                mask2 = mask1 | (1 << k)

                p =  n ^ mask2
                if lut[n][6] == lut[p][6]:
                    s = '{}{}{}{}{}{}'.format(lut[p][0],lut[p][1],lut[p][2],lut[p][3],lut[p][4],lut[p][5])
                    input_sequence.add(s)
##                    print (bin(n)[2:].zfill(6)[:3],     bin(n)[2:].zfill(6)[3:], '  |  ',
##                           bin(mask1)[2:].zfill(6)[:3], bin(mask1)[2:].zfill(6)[3:], '  |  ',
##                           bin(p)[2:].zfill(6)[:3],     bin(p)[2:].zfill(6)[3:], '  |  ',
##                           lut[n][6] == lut[p][6])

    all_combinations = set(combinations(input_sequence, 8))
##    print(input_sequence)
##    results = set()
    for combination in all_combinations:
        result = find_mask(combination)
        if (result.count('x') == 3):
            results.add(result)
            flag = True
            #print(combination, end=' -- ')
            #print(result)
    return flag
##    for result in results:
##        print(result)


def get_n4 (n):
    global lut
    global results
    flag = False

    input_sequence=set()
    s = '{}{}{}{}{}{}'.format(lut[n][0],lut[n][1],lut[n][2],lut[n][3],lut[n][4],lut[n][5])
    input_sequence.add(s)

    for i in range(6):
        mask = 1 << i
        for j in range(i, 6):
            mask1 = mask | (1 << j)
            for k in range (j, 6):
                mask2 = mask1 | (1 << k)
                for l in range (k, 6):
                    mask3 = mask2 | (1 << l)

                    p =  n ^ mask3
                    if lut[n][6] == lut[p][6]:
                        s = '{}{}{}{}{}{}'.format(lut[p][0],lut[p][1],lut[p][2],lut[p][3],lut[p][4],lut[p][5])
                        input_sequence.add(s)
    print(input_sequence)
    all_combinations = set(combinations(input_sequence, 16))

    for combination in all_combinations:
        result = find_mask(combination)
        if (result.count('x') == 4):
            results.add(result)
            flag = True
    return flag

def main():
    global lut
    global results

    lut = init_lut()

    lut[40]=[1,1,1,0,0,0,1]
    lut[41]=[1,1,1,0,0,1,1]
    lut[42]=[1,1,1,0,1,0,1]
    lut[43]=[1,1,1,0,1,1,1]
    lut[44]=[1,1,1,1,0,0,1]
    lut[45]=[1,1,1,1,0,1,1]
    lut[46]=[1,1,1,1,1,0,1]
    lut[47]=[1,1,1,1,1,1,1]

#    print(lut)
    # Генерируем код Грея для 6 разрядов
    gray_code_6_bit = generate_gray_code(2)

    maps = '0110101110110000111000111011100001011010101010111110000011100000'
    maps = '1111000001111001001011111111111111111111111111111111111111111111'
    print(maps)
    for i in range(len(maps)):
        print(maps[i], end='')
        if (i + 1) % 8 == 0:
            print()

    print()
    print('    | ', end='')
    for code1 in gray_code_6_bit:
        print(code1, end=' ')
    print()
    print('--------------------------------------')

    index = 0
    for code in gray_code_6_bit:
        print(code, end=' | ')
        for code1 in gray_code_6_bit:
            binary_string = code + code1
            integer_value = int(binary_string, 2)
            lut[integer_value][6] = int(maps[index])
            index += 1
            print("{: 3d}".format(lut[integer_value][6]), end=' ')
##            print("{:03d}".format(integer_value), end=' ')
        print()

    i = 0
    print('    | ', end='')
    for code1 in gray_code_6_bit:
        print(code1, end=' ')
    print()
    print('--------------------------------------')

    for code in gray_code_6_bit:
        print(code, end=' | ')
        for code1 in gray_code_6_bit:
            binary_string = code + code1
            integer_value = int(binary_string, 2)
            print("{:03d}".format(integer_value), end=' ')
        print()

    print()
    print('    | ', end='')
    for code1 in gray_code_6_bit:
        print(code1, end=' ')
    print()
    print('--------------------------------------')

    for code in gray_code_6_bit:
        print(code, end=' | ')
        for code1 in gray_code_6_bit:
            binary_string = code + code1
            integer_value = int(binary_string, 2)
##            print("{:03d}".format(lut[integer_value][6]), end=' ')
            print("{: 3d}".format(lut[integer_value][6]), end=' ')
        print()

##
##    for i in range(64):
##        get_n2(i)
####
##    print('    | ', end='')
##    for code1 in gray_code_6_bit:
##        print(code1, end=' ')
##    print()
##    print('--------------------------------------')
##
##    for code in gray_code_6_bit:
##        print(code, end=' | ')
##        for code1 in gray_code_6_bit:
##            binary_string = code + code1
##            integer_value = int(binary_string, 2)
##            print("{: 3d}".format(lut[integer_value][6]), end=' ')
##        print()
##
##
    print()
    f1 = False
    f2 = False
    f3 = False
    f4 = False
    print('search x')
    for i in range(64):
        print(i, end='')
        #f1 = f1 | get_n1(i)

    if f1:
        print()
        print('search xx')
        for i in range(64):
            print(i, end='')
            #f2 = f2 | get_n2(i)

    if not(f2):
        print()
        print('search xxx')
        for i in range(64):
            print(i, end='')
            f3 = f3 | get_n3(i)

    if f3:
        print()
        print('search xxxx')
        for i in range(64):
            print(i, end='')
            get_n4(i)

    print()
##
    print('    | ', end='')
    for code1 in gray_code_6_bit:
        print(code1, end=' ')
    print()
    print('--------------------------------------')

    for code in gray_code_6_bit:
        print(code, end=' | ')
        for code1 in gray_code_6_bit:
            binary_string = code + code1
            integer_value = int(binary_string, 2)
            print("{: 3d}".format(lut[integer_value][6]), end=' ')
        print()

    for result in results:
        print(result, end=' - ')
        r = ''
        for i in result:
            if i == 'x':
                r += '1'
            else:
                r += i
        rn = int(r, 2)
        print(lut[rn][6])

    pass


if __name__ == '__main__':
    main()
