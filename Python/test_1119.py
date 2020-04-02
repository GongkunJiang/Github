"""
    Author: Dell
    Time: 2019/11/19 14:18
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
    # if len(binary) < 114:
    #     print(len(binary))
    retain = binary[-precision:]
    # abandon = '0' * (precision - len(binary[:-precision])) + binary[:-precision]
    abandon = bin(fill)[2:2 + precision - len(binary[:-precision])] + binary[:-precision]
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
        le += mt.log(abs(func(x) - func((x + 1) % domain)))
        x = func(x)
    le /= 10000
    return le


if __name__ == '__main__':
    precision = 16
    domain = 2 ** precision
    fill = random.randint(1, domain)
    # lyapunov_exponent = LE()
    x0 = random.randint(1, domain)
    x1 = x0
    data = []
    for i in range(10000):
        x1 = func(x1)
        data.append(x1)
    plt.scatter(data, [i for i in range(10000)], marker=',', s=1, linewidths=0.1, c='b')
    plt.show()

    # for mu in range(1, domain):
    #     x1 = x0
    #     data = []
    #     print(mu)
    #     for i in range(10000):
    #         x2 = int(inverse(bin(x1)[2:]), 2)
    #         x1 = m(x1, x2)
    #         data.append(x1)
    #     plt.hist(data, domain - 1, color='b', density=1)
    #     plt.title(mu)
    #     plt.show()

    # data = []
    # for x1 in range(1, domain):
    #     for x2 in range(1, domain):
    #         x3 = m(x1, x2)
    #         # print("%d,%d,%d" % (x1, x2, x3))
    #         data.append(x3)
    # plt.hist(data, domain - 1, color='b', density=1)
    # plt.show()
