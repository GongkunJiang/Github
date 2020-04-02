"""
    Author: Dell
    Time: 2019/11/14 15:06
"""
"""
    Author: Dell
    Time: 2019/11/14 13:08
"""
import random
import math as mt
import matplotlib.pyplot as plt


def BigLogistic(x):
    y = 4 * x - ((4 * x * x) >> 64)
    # print(bin(y))
    # z = int(bin(y)[2:Bit + 2], 2)
    # a = y % (2 ** Bit)
    return y


def BL_diff(x, mu=1):
    y = 4 - x >> (64 - 3)
    return y


if __name__ == '__main__':
    # # Bit位大整数
    # Bit = 64
    # x0 = random.randint(0, 2 ** Bit - 1)
    # mu = 4 / (2 ** Bit)
    # x = x0
    # le = 0
    # for count in range(10000):
    #     # print(count)
    #     # le += mt.log(abs(BL_diff(x, mu)))
    #     x = BigLogistic(x, mu)
    #     print(x)
    # # le /= 10000
    # # print(le)

    B = 2 ** 64
    x = random.randint(1, 2 ** 64 - 1)
    for i in range(100):
        x = BigLogistic(x)
        print(x)

    le = 0
    for count in range(100000):
        # print(count)
        le += mt.log(abs(BL_diff(x)))
        x = BigLogistic(x)
        print(x)
    le /= 100000
    print(le)
