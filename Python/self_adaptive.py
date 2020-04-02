"""
    Author: Dell
    Time: 2019/11/13 17:02
"""
import numpy as np

if __name__ == '__main__':
    a = np.random.rand(8, 8)
    b = a.copy()[:4]
    c = a.copy()[4:]
    order_b = np.array(sorted(b.flatten())).reshape(4, 8)
    b_, c_ = np.zeros((4, 4)), np.zeros((4, 4))
    # index = np.argwhere(b == d[0])
