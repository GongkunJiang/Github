"""
    Author: Dell
    Time: 2019/9/23 13:58
"""
import numpy as np

if __name__ == '__main__':

    matrix = np.array([i for i in range(25)]).reshape((5, 5))
    sequence = [np.random.random() for i in range(10)]

    dic_P, dic_Q = {}, {}
    for i in range(matrix.shape[0]):
        dic_P[sequence[i]] = i
    for j in range(matrix.shape[1]):
        dic_Q[sequence[matrix.shape[0] + j]] = j
    order_P = [dic_P[k] for k in sorted(dic_P.keys())]
    order_Q = [dic_Q[k] for k in sorted(dic_Q.keys())]

    matrix_P = np.zeros((matrix.shape[0], matrix.shape[0]))
    matrix_Q = np.zeros((matrix.shape[1], matrix.shape[1]))
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[0]):
            if order_P[i] == j:
                matrix_P[i][j] = 1
    for i in range(matrix.shape[1]):
        for j in range(matrix.shape[1]):
            if order_Q[i] == j:
                matrix_Q[i][j] = 1

    result = np.dot(np.dot(matrix_P, matrix), matrix_Q)



    # if not inverse:
    #     return np.dot(np.dot(matrix_P, matrix), matrix_Q)
    # else:
    #     return np.dot(np.dot(matrix_P.T, matrix), matrix_Q.T)
