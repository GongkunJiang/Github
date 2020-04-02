"""
    Author: Dell
    Time: 2019/11/24 16:50
"""

import random
import numpy as np
import math as mt
import os


def xor(s1, s2):
    result = ''
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            result += '0'
        else:
            result += '1'
    return result


def And(s1, s2):
    result = ''
    for i in range(len(s1)):
        if s1[i] == s2[i] == '1':
            result += '1'
        else:
            result += '0'
    return result


def Or(s1, s2):
    result = ''
    for i in range(len(s1)):
        if s1[i] == s2[i] == '0':
            result += '0'
        else:
            result += '1'
    return result


def inverse(s):
    result = ''
    for i in range(len(s)):
        if s[i] == '0':
            result += '1'
        elif s[i] == '1':
            result += '0'
    if len(result) < precision:
        result = '1' * (precision - len(result)) + result
    return result


def m(m1, m2):
    product = m1 * m2
    binary = bin(product)[2:]
    if len(binary) < 2 * precision:
        binary = '0' * (2 * precision - len(binary)) + binary
    retain = binary[-precision:]
    abandon = binary[:-precision]
    result = xor(retain, abandon)
    return int(result, 2)


def func(x):
    return m(x, domain - x)


if __name__ == '__main__':
    precision = 64
    domain = 2 ** precision
    x = 15125645981407076156
    piece = 56
    wrote = 0
    length = 10 ** 9
    if os.path.exists('./data_06.txt'):
        os.remove('./data_06.txt')
    for i in range(100):
        x = func(x)
    with open(r'./data_06.txt', 'a') as f:
        while wrote < length:
            if wrote % 1000000 == 0:
                print(int((length - wrote) / 1000000))
            x = func(x)
            string = '0' * (precision - len(bin(x)[2:])) + bin(x)[2:]
            f.write(string[-piece:])
            wrote += piece