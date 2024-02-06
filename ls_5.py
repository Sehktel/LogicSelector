#-------------------------------------------------------------------------------
# Name:        Logic Selector f(ABCDE)
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


rows, cols = (32, 6)
lut = [[0]*cols for _ in range(rows)]
results_1 = set()
results_0 = set()

def init_lut():
    nums = [[0]*cols]*rows

    for i in range(32):
        E = (i >> 0) & int('00000001', 2)
        D = (i >> 1) & int('00000001', 2)
        C = (i >> 2) & int('00000001', 2)
        B = (i >> 3) & int('00000001', 2)
        A = (i >> 4) & int('00000001', 2)
        # print(A,B,C,D,E)
        nums[i] = [A, B, C, D, E, random.randint(0, 1)]

        print(nums[i])
    return nums
        # pass

def generate_gray_code(n):
    if n <= 0:
        return []

    gray_code = ['0', '1']

    for i in range(1, n):
        print (i)
        for j in range(len(gray_code) - 1, -1, -1):
            gray_code.append(gray_code[j])

        for j in range(len(gray_code) // 2):
            gray_code[j] = '0' + gray_code[j]
        for j in range(len(gray_code) // 2, len(gray_code)):
            gray_code[j] = '1' + gray_code[j]

    return gray_code


def find_mask(sequence, mask):
    length = len(sequence[0])
    common_mask = ""
    for i in range(length):
        if all(s[i] == sequence[0][i] for s in sequence):
            common_mask += sequence[0][i]
        else:
            common_mask += "x"
    return common_mask

def find_mask1(sequence):
    length = len(sequence[0])
    common_mask = ""
    for i in range(length):
        if all(s[i] == sequence[0][i] for s in sequence):
            common_mask += sequence[0][i]
        else:
            if sequence[0][i] == 'x' or sequence[1][i] == 'x':
                common_mask += "x"
            else:
                common_mask += "t"

    return common_mask

def find_mask2(sequence):
    length = len(sequence[0])
    common_mask = ""
    for i in range(length):
        if all(s[i] == sequence[0][i] for s in sequence):
            common_mask += sequence[0][i]
        else:
            if sequence[0][i] == 'x' and sequence[1][i] == 't':
                common_mask += "x"
            elif sequence[0][i] == 't' and sequence[1][i] == 'x':
                common_mask += "x"
            else:
                common_mask += "x"

    return common_mask

def get_n ():
    global lut
    global results_0
    global results_1

    input_sequence_0 = set()
    input_sequence_1 = set()

    for n in range(32):
        s = '{}{}{}{}{}'.format(lut[n][0],lut[n][1],lut[n][2],lut[n][3],lut[n][4])
        if lut[n][5]:
            input_sequence_1.add(s)
        else:
            input_sequence_0.add(s)

    input_sequence1_0 = set()
    all_combinations1_0 = set(combinations(input_sequence_0, 2))
    for combination in all_combinations1_0:
        result = find_mask(combination, '')
        if (result.count('x') == 1):
            input_sequence1_0.add(result)

    input_sequence2_0 = set()
    all_combinations2_0 = set(combinations(input_sequence1_0, 2))
    for combination in all_combinations2_0:
        result = find_mask1(combination)
        if (result.count('t') == 1 and result.count('x') == 1) :
            input_sequence2_0.add(result)
## Фильтрация
    all_combinations21_0 = set(combinations(input_sequence2_0,2))
    input_sequence2_0.clear()
    for combination in all_combinations21_0:
        result = find_mask2(combination)
        if (result.count('x') == 2 and result.count('t') == 0) :
            input_sequence2_0.add(result)


    input_sequence4_0 = set()
    all_combinations4_0 = set(combinations(input_sequence2_0, 2))
    for combination in all_combinations4_0:
        result = find_mask1(combination)
        if (result.count('t') == 1 and result.count('x') == 2) :
            input_sequence4_0.add(result)
    all_combinations41_0 = set(combinations(input_sequence4_0,2))
    input_sequence4_0.clear()
    for combination in all_combinations41_0:
        result = find_mask2(combination)
        if (result.count('x') == 3 and result.count('t') == 0) :
            input_sequence4_0.add(result)


    input_sequence8_0 = set()
    all_combinations8_0 = set(combinations(input_sequence4_0, 2))
    for combination in all_combinations8_0:
        result = find_mask1(combination)
        if (result.count('t') == 1 and result.count('x') == 3) :
            input_sequence8_0.add(result)
    all_combinations81_0 = set(combinations(input_sequence8_0,2))
    input_sequence8_0.clear()
    for combination in all_combinations81_0:
        result = find_mask2(combination)
        if (result.count('x') == 4 and result.count('t') == 0) :
            input_sequence8_0.add(result)


    input_sequence16_0 = set()
    all_combinations16_0 = set(combinations(input_sequence8_0, 2))
    for combination in all_combinations16_0:
        result = find_mask1(combination)
        if (result.count('t') == 1 and result.count('x') == 4) :
            input_sequence16_0.add(result)
    all_combinations161_0 = set(combinations(input_sequence16_0,2))
    input_sequence16_0.clear()
    for combination in all_combinations161_0:
        result = find_mask2(combination)
        if (result.count('x') == 5  and result.count('t') == 0) :
            input_sequence16_0.add(result)


    input_sequence32_0 = set()
    all_combinations32_0 = set(combinations(input_sequence16_0, 2))
    for combination in all_combinations32_0:
        result = find_mask1(combination)
        if (result.count('t') == 1 and result.count('x') == 5) :
            input_sequence32_0.add(result)
    all_combinations321_0 = set(combinations(input_sequence32_0,2))
    input_sequence32_0.clear()
    for combination in all_combinations321_0:
        result = find_mask2(combination)
        if (result.count('x') == 6  and result.count('t') == 0) :
            input_sequence32_0.add(result)

    input_sequence1_1 = set()
    all_combinations1_1 = set(combinations(input_sequence_1, 2))
    for combination in all_combinations1_1:
        result = find_mask(combination, '')
        if (result.count('x') == 1):
            input_sequence1_1.add(result)

    input_sequence2_1 = set()
    all_combinations2_1 = set(combinations(input_sequence1_1, 2))
    for combination in all_combinations2_1:
        result = find_mask1(combination)
        if (result.count('t') == 1 and result.count('x') == 1) :
            input_sequence2_1.add(result)
## Фильтрация
    all_combinations21_1 = set(combinations(input_sequence2_1,2))
    input_sequence2_1.clear()
    for combination in all_combinations21_1:
        result = find_mask2(combination)
        if (result.count('x') == 2 and result.count('t') == 0) :
            input_sequence2_1.add(result)


    input_sequence4_1 = set()
    all_combinations4_1 = set(combinations(input_sequence2_1, 2))
    for combination in all_combinations4_1:
        result = find_mask1(combination)
        if (result.count('t') == 1 and result.count('x') == 2) :
            input_sequence4_1.add(result)
    all_combinations41_1 = set(combinations(input_sequence4_1,2))
    input_sequence4_1.clear()
    for combination in all_combinations41_1:
        result = find_mask2(combination)
        if (result.count('x') == 3 and result.count('t') == 0) :
            input_sequence4_1.add(result)


    input_sequence8_1 = set()
    all_combinations8_1 = set(combinations(input_sequence4_1, 2))
    for combination in all_combinations8_1:
        result = find_mask1(combination)
        if (result.count('t') == 1 and result.count('x') == 3) :
            input_sequence8_1.add(result)
    all_combinations81_1 = set(combinations(input_sequence8_1,2))
    input_sequence8_1.clear()
    for combination in all_combinations81_1:
        result = find_mask2(combination)
        if (result.count('x') == 4 and result.count('t') == 0) :
            input_sequence8_1.add(result)


    input_sequence16_1 = set()
    all_combinations16_1 = set(combinations(input_sequence8_1, 2))
    for combination in all_combinations16_1:
        result = find_mask1(combination)
        if (result.count('t') == 1 and result.count('x') == 4) :
            input_sequence16_1.add(result)
    all_combinations161_1 = set(combinations(input_sequence16_1,2))
    input_sequence16_1.clear()
    for combination in all_combinations161_1:
        result = find_mask2(combination)
        if (result.count('x') == 5  and result.count('t') == 0) :
            input_sequence16_1.add(result)


    input_sequence32_1 = set()
    all_combinations32_1 = set(combinations(input_sequence16_1, 2))
    for combination in all_combinations32_1:
        result = find_mask1(combination)
        if (result.count('t') == 1 and result.count('x') == 5) :
            input_sequence32_1.add(result)
    all_combinations321_1 = set(combinations(input_sequence32_1,2))
    input_sequence32_1.clear()
    for combination in all_combinations321_1:
        result = find_mask2(combination)
        if (result.count('x') == 6  and result.count('t') == 0) :
            input_sequence32_1.add(result)

    print()
    if len(input_sequence1_0) :
        print()
        print('input_sequence1_0', input_sequence1_0)
    if len(input_sequence1_1) :
        print()
        print('input_sequence1_1', input_sequence1_1)

    if len(input_sequence2_0) :
        print()
        print('input_sequence2_0', input_sequence2_0)
    if len(input_sequence2_1) :
        print()
        print('input_sequence2_1', input_sequence2_1)

    if len(input_sequence4_0) :
        print()
        print('input_sequence4_0', input_sequence4_0)
    if len(input_sequence4_1) :
        print()
        print('input_sequence4_1', input_sequence4_1)

    if len(input_sequence8_0) :
        print()
        print('input_sequence8_0', input_sequence8_0)
    if len(input_sequence8_1) :
        print()
        print('input_sequence8_1', input_sequence8_1)

    if len(input_sequence16_0) :
        print()
        print('input_sequence16_0', input_sequence16_0)
    if len(input_sequence16_1) :
        print()
        print('input_sequence16_1', input_sequence16_1)

    if len(input_sequence32_0) :
        print()
        print('input_sequence32_0', input_sequence32_0)
    if len(input_sequence32_1) :
        print()
        print('input_sequence32_1', input_sequence32_1)

def main():
    global lut
    global results

    lut = init_lut()

#    print(lut)
    # Генерируем код Грея для 6 разрядов
    gray_code_2_bit = generate_gray_code(2)
    gray_code_3_bit = generate_gray_code(3)

#    maps = '01101011101100001110001110111000'
## 01011010101010111110000011100000'
##    maps = '11110000011110010010111111111111'
#    maps = '11111111111111111111111111111111'

#  Parser карт Карно Раскомментировать в случсе острой необходимости
##    print(maps)
##    for i in range(len(maps)):
##        print(maps[i], end='')
##        if (i + 1) % 8 == 0:
##            print()
##
##    print()
##    print('    | ', end='')
##    for code1 in gray_code_3_bit:
##        print(code1, end=' ')
##    print()
##    print('--------------------------------------')
##
##    index = 0
##    for code in gray_code_2_bit:
##        print(code, end=' | ')
##        for code1 in gray_code_3_bit:
##            binary_string = code + code1
##            integer_value = int(binary_string, 2)
##            lut[integer_value][5] = int(maps[index])
##            index += 1
##            print("{: 3d}".format(lut[integer_value][5]), end=' ')
####            print("{:03d}".format(integer_value), end=' ')
##        print()


    i = 0
    print('    | ', end='')
    for code1 in gray_code_3_bit:
        print(code1, end=' ')
    print()
    print('--------------------------------------')

    for code in gray_code_2_bit:
        print(code, end=' | ')
        for code1 in gray_code_3_bit:
            binary_string = code + code1
            integer_value = int(binary_string, 2)
            print("{:03d}".format(integer_value), end=' ')
        print()

    print()
    print('    | ', end='')
    for code1 in gray_code_3_bit:
        print(code1, end=' ')
    print()
    print('--------------------------------------')

    for code in gray_code_2_bit:
        print(code, end=' | ')
        for code1 in gray_code_3_bit:
            binary_string = code + code1
            integer_value = int(binary_string, 2)
##            print("{:03d}".format(lut[integer_value][6]), end=' ')
            print("{: 3d}".format(lut[integer_value][5]), end=' ')
        print()

    get_n()

    for result in results_0:
        print(result, ' -- 0')
    print()
    print('--------------------------------------')
    for result in results_1:
        print(result, ' -- 1')

    pass


if __name__ == '__main__':
    main()
