"""
    Author: Dell
    Time: 2019/11/24 16:50
"""

import random
import numpy as np
import matplotlib.pyplot as plt
import math as mt


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
    # x = random.randint(1, domain)
    x = 15125645981407076156
    iteration = int(1.6 * 10 ** 7)  # 10**9/64 = 5625000.0
    for i in range(100):
        x = func(x)
    c = []
    # iteration = 10 ** 5
    for j in range(iteration):
        if j % 10000 == 0:
            print("%d" % ((iteration - j) / 10000))
        x = func(x)
        string = '0' * (precision - len(bin(x)[2:])) + bin(x)[2:]
        X = [string[j * 8:(j + 1) * 8] for j in range(int(len(string) / 8))]
        Y = xor(X[0], X[-1]) + xor(X[1], X[-2]) + xor(X[2], X[-3]) + xor(X[3], X[-4]) + \
            xor(X[4], X[-1][::-1]) + xor(X[5], X[-2][::-1]) + xor(X[6], X[-3][::-1]) + xor(X[7], X[-4][::-1])
        with open(r'./data_03.txt', 'a') as f:
            f.write(Y)
    #     c.append(Y.count('0') / len(Y))
    # print(np.mean(c))
