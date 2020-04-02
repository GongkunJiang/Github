"""
    Author: Administrator
    Time: 2019/11/27 21:42
"""
import struct
from shutil import copyfile
import os


def xor(s1, s2):
    result = ''
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            result += '0'
        else:
            result += '1'
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
    for i in range(100):
        x = func(x)
    length = [2 ** 20, 2 ** 25, 2 ** 30]
    path = [r'./TestU01_04_220.bin', r'./TestU01_04_225.bin', r'./TestU01_04_230.bin']
    wrote = 0
    piece = 56
    if os.path.exists(path[0]):
        os.remove(path[0])
    for amount in range(3):
        with open(path[amount], 'ab+') as f:
            while wrote < length[amount]:
                if wrote % 1000000 == 0:
                    print(int((length[amount] - wrote) / 1000000))
                x = func(x)
                string = '0' * (precision - len(bin(x)[2:])) + bin(x)[2:]
                y = string[-piece:]
                for n in range(int(piece / 8)):
                    f.write(struct.pack('B', int(y[n * 8:(n + 1) * 8], 2)))
                    wrote += 8
        print("第%d个文件写入完成！！！" % (amount + 1))
        if amount < 2:
            copyfile(path[amount], path[amount + 1])
