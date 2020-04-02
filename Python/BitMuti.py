"""
    Author: Dell
    Time: 2019/11/14 15:38
"""
import random
import matplotlib.pyplot as plt


def function(x0, y0, precision):
    x1 = bin(x0 * y0)[precision + 2:] + '0' * (precision - len(bin(x0 * y0)[precision + 2:]))
    x0 = x0 ^ int(x1, 2)
    y1 = bin(x0 * y0)[precision + 2:] + '0' * (precision - len(bin(x0 * y0)[precision + 2:]))
    y0 = y0 ^ int(y1, 2)
    return x0, y0


if __name__ == '__main__':
    precision = 8
    x0 = random.randint(1, 2 ** precision - 1)
    y0 = random.randint(1, 2 ** precision - 1)
    X, Y = [], []
    x, y = x0, y0
    for i in range(10 ** 5):
        x, y = function(x, y, precision)
        X.append(x)
        Y.append(y)
    plt.hist(X, 200, color='b', density=1)
    plt.show()
