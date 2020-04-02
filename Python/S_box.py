"""
    Author: Dell
    Time: 2019/11/22 12:48
"""
import random


def xor(s1, s2):
    result = ''
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            result += '0'
        else:
            result += '1'
    return result


def BigIntLogistic(x):
    if x == 0:
        return 2 ** 128 - 1
    else:
        return int(x * (2 ** 128 - x) / 2 ** 126)


def Tent(a, x):
    if 0 <= x <= a:
        return x / a
    elif a < x <= 1:
        return (1 - x) / (1 - a)


if __name__ == '__main__':
    s_box = []
    x0 = random.randint(1, 2 ** 128 - 1)
    x1 = x0
    for i in range(100):
        x1 = BigIntLogistic(x1)

    while len(s_box) < 256:
        binary = '0' * (128 - len(bin(x1)[2:])) + bin(x1)[2:]
        X = []
        for j in range(16):
            X.append(binary[j * 8:(j + 1) * 8])
        y = '00000000'
        for k in X:
            y = xor(y, k)
        if y not in s_box:
            s_box.append(int(y, 2))
        x1 = BigIntLogistic(int(''.join(X[::-1]), 2))

    a, x0 = random.random(), random.random()
