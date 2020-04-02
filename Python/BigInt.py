"""
    Author: Dell
    Time: 2019/11/14 13:08
"""
import random
import math as mt
import matplotlib.pyplot as plt


def BigLogistic(x, mu=4):
    y = int(mu * x * (1 - x * (2 ** (-64))))
    # print(bin(y))
    # z = int(bin(y)[2:Bit + 2], 2)
    # a = y % (2 ** Bit)
    return y


def BL_diff(x, mu=1):
    y = mu * (1 - x * (2 ** (-63)))
    return y


if __name__ == '__main__':

    # Bit位大整数
    Bit = 64
    x0 = random.randint(0, 2 ** Bit - 1)
    mu = 4/(2**Bit)
    x = x0
    le = 0
    for count in range(10000):
        # print(count)
        # le += mt.log(abs(BL_diff(x, mu)))
        x = BigLogistic(x, mu)
        print(x)
    # le /= 10000
    # print(le)
