"""
    Author: Dell
    Time: 2019/11/20 19:40
"""
import random
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
    # m1 = random.randint(1, domain)
    # m2 = int(inverse(bin(m1)[2:]), 2)
    product = m1 * m2
    binary = bin(product)[2:]
    if len(binary) < 2*precision:
        binary = '0' * (2*precision - len(binary)) + binary
    retain = binary[-precision:]
    abandon = binary[:-precision]
    result = xor(retain, abandon)
    return int(result, 2)


def func(x):
    reverse_x = int(inverse(bin(x)[2:]), 2)
    # result = x * reverse_x
    result = m(x, reverse_x)
    return result  # >> (precision - 2)


def LE():
    # x = 1221773908319746789
    x = random.randint(1, domain)
    le = 0
    for count in range(10000):
        difference_value = func(x) - func((x + 1) % domain)
        if difference_value == 0:
            x = func(x)
            continue
        else:
            le += mt.log(abs(difference_value))
            x = func(x)
    le /= 10000
    return le


if __name__ == '__main__':
    precision = 2
    P, Lyapunov_exponent = [], []
    while precision <= 100:
        print(precision)
        domain = 2 ** precision
        fill = random.randint(1, domain)
        P.append(precision)
        Lyapunov_exponent.append(LE())
        precision += 2
    plt.plot(P, Lyapunov_exponent, marker='.', linestyle='-', c='b')
    plt.ylabel("Lyapunov exponent", fontsize='16')
    plt.xlabel("Precision", fontsize='16')
    plt.show()
