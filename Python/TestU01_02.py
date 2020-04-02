"""
    Author: Administrator
    Time: 2019/11/27 21:42
"""
import struct
from shutil import copyfile


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
    path = [r'./TestU01_02_220.bin', r'./TestU01_02_225.bin', r'./TestU01_02_230.bin']
    wrote = 0
    with open(path[0], 'ab+') as f:
        while wrote < length[0]:
            if wrote % 1000000 == 0:
                print("%d" % ((length[0] - wrote) / 1000000))
            x = func(x)
            string = '0' * (precision - len(bin(x)[2:])) + bin(x)[2:]
            X = [string[j * 8:(j + 1) * 8] for j in range(int(len(string) / 8))]
            y = '00000000'
            for k in X:
                y = xor(y, k)
            f.write(struct.pack('B', int(y, 2)))
            wrote += 8
    print("第一个文件写入完成！！！")
    copyfile(path[0], path[1])
    with open(path[1], 'ab+') as f:
        while wrote < length[1]:
            if wrote % 1000000 == 0:
                print("%d" % ((length[1] - wrote) / 1000000))
            x = func(x)
            string = '0' * (precision - len(bin(x)[2:])) + bin(x)[2:]
            X = [string[j * 8:(j + 1) * 8] for j in range(int(len(string) / 8))]
            y = '00000000'
            for k in X:
                y = xor(y, k)
            f.write(struct.pack('B', int(y, 2)))
            wrote += 8
    print("第二个文件写入完成！！！")
    copyfile(path[1], path[2])
    with open(path[2], 'ab+') as f:
        while wrote < length[2]:
            if wrote % 1000000 == 0:
                print("%d" % ((length[2] - wrote) / 1000000))
            x = func(x)
            string = '0' * (precision - len(bin(x)[2:])) + bin(x)[2:]
            X = [string[j * 8:(j + 1) * 8] for j in range(int(len(string) / 8))]
            y = '00000000'
            for k in X:
                y = xor(y, k)
            f.write(struct.pack('B', int(y, 2)))
            wrote += 8
    print("第三个文件写入完成！！！")
