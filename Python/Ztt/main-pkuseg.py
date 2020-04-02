#!/user/bin/env python
# -*- encoding=utf-8 -*-

# 导入文件

import random
import math
import copy
import operator


# 元祖提取
# def tupleExprt():
#     arr = [] #元祖集合;
#     f = open("./删除之后的.txt","r",encoding='utf-8-sig')
#     lines = f.readlines()
#     for line in lines:
#         # print(content);
#         #  line1 = "".join(line)
#         s_list = line.split(' ')
#         if '\n' in s_list[-1]:
#             s_list[-1]=s_list[-1].replace('\n','')
#         tagsN, tagsA, tagsV = [], [], []
#         for item in s_list:
#             if item.endswith('/n'):
#                 tagsN.append(item[:-2])
#             if item.endswith('/v'):
#                 tagsV.append(item[:-2])
#             if item.endswith('/a'):
#                 tagsA.append(item[:-2])
#             for i in tagsN:
#               for j in tagsA:
#                arr.append((tagsN[i],tagsA[j]))
#             for i1 in tagsN:
#               for j1 in tagsV:
#                arr.append((tagsN[i1],tagsV[j1]))
#         return arr
def tupleExprt():
    all_N, all_A, all_V = [], [], []
    f = open("./删除之后的.txt", "r", encoding='utf-8-sig')
    lines = f.readlines()
    for line in lines:
        s_list = line.split(' ')
        if '\n' in s_list[-1]:
            s_list[-1] = s_list[-1].replace('\n', '')
        tagsN, tagsA, tagsV = [], [], []
        for item in s_list:
            if item.endswith('/n'):
                tagsN.append(item[:-2])
            if item.endswith('/v'):
                tagsV.append(item[:-2])
            if item.endswith('/a'):
                tagsA.append(item[:-2])
        all_A.append(tagsA)
        all_V.append(tagsV)
        all_N.append(tagsN)
    all_n_a = []
    all_n_v = []
    for i in range(len(all_A)):
        # 对每一行进行操作
        tmp_a = all_A[i]
        tmp_v = all_V[i]
        tmp_n = all_N[i]

        n_a = []
        n_v = []
        for n in tmp_n:
            for a in tmp_a:
                n_a.append((n, a))
            for v in tmp_v:
                n_v.append((n, v))
        all_n_a.append(n_a)
        all_n_v.append(n_v)
    result = sum(all_n_a, []) + sum(all_n_v, [])
    result = set(result)
    return result


def readVector():
    vec = {}
    f = open("./vectors.txt", "r", encoding='utf-8-sig')
    lines = f.readlines()
    for line in lines:
        arr = line.split(" ")
        vec.setdefault(arr[0], arr[1:])
    return vec


# 将元祖转化为向量
def dataProccess(Ctuple, vec):
    # 词性冲突
    print(Ctuple[0])
    # result = vec[Ctuple[0]] + vec[Ctuple[1]]
    result = 0
    return result


# 所有元祖的向量子点
def allTupleVec(allTuple, vec):
    d = {}
    for t in allTuple:
        key = str(t[0] + t[1])
        d.setdefault(key, dataProccess(t, vec))
    return d


# K-MEANS
# 距离公式：欧几里德距离
def dist(x, y):
    # tmp = zip(x,y)
    sum = 0
    # for x,y in tmp:
    L = len(x)
    for i in range(L):
        sum += math.pow(float(x[i]) - float(y[i]), 2)
    result = math.sqrt(sum)
    return result


def Kmeans(C_num, UserRatingDistribution):
    # 定义簇集合Set1,Set2,...,SetK
    print("正在初始化集合......")
    Cluster = {}
    for j in range(C_num):
        Cluster.setdefault("Cluster" + str(j + 1), {})
    # 先随机C_num个样本作为初始中心点
    print("正在初始化中心点......")
    center = {}
    keys = random.sample(UserRatingDistribution.keys(), C_num)
    for i in range(C_num):
        key = keys[i]
        center.setdefault("c" + str(i + 1), UserRatingDistribution[key])
    print("初始中心点集合为：")
    # print(center)
    for k in center.keys():
        print(center[k])
    pre_center = {}
    current_center = copy.deepcopy(center)
    flag = 1
    while operator.eq(pre_center, current_center) == False:
        print("-------------------------------------------------------------------------")
        print("开始进行第" + str(flag) + "次迭代")
        # 对Cluster先清空
        for h in range(C_num):
            Cluster["Cluster" + str(h + 1)] = {}
        pre_center = copy.deepcopy(current_center)
        # 对数据考察一遍得到初始划分簇
        for u in UserRatingDistribution.keys():
            distance = {}
            for c in current_center.keys():
                d = dist(UserRatingDistribution[u], current_center[c])
                distance.setdefault(c, d)
            key_name = min(distance, key=distance.get)
            clu_number = list(filter(str.isdigit, key_name))
            clu_name = "Cluster" + str(clu_number[0])
            Cluster[clu_name].setdefault(u, UserRatingDistribution[u])
        print("正在根据中心点集合划分簇.....")
        for c in Cluster.keys():
            print(len(Cluster[c]))
        # 对中心点进行更新
        for c in pre_center.keys():
            number = list(filter(str.isdigit, c))[0]
            Cluster_set = Cluster["Cluster" + str(number)]
            # print(Cluster_set)
            mid_s = [0 for x in range(600)]
            for u in Cluster_set.keys():
                mid_s = [float(mid_s[x]) + float(Cluster_set[u][x]) for x in range(600)]
            current_center[c] = [float(x) * 1.0 / len(Cluster_set.keys()) for x in mid_s]
        print("更新前中心点集合为：")
        # print(pre_center)
        for key in pre_center.keys():
            print(pre_center[key])
        print("更新后中心点集合为：")
        # print(current_center)
        for key in current_center.keys():
            print(current_center[key])
        flag += 1
    print("中心点向量未更新，迭代终止")
    # print(Cluster)
    return current_center


# 寻找隐性特征词
def keyWord(center, vec):
    result = []
    for c in center.keys():
        # print(center[c])
        d = {}
        current_center = center[c][0:300]
        for k in vec.keys():
            d_kc = dist(current_center, vec[k])
            d.setdefault(k, d_kc)
        minwordkey = min(d, key=d.get)
        result.append(minwordkey)
    print(result)


if __name__ == '__main__':
    C_num = 3
    vec = readVector()
    allTuple = tupleExprt()
    distribution = allTupleVec(allTuple, vec)
    center = Kmeans(C_num, distribution)
    keyWord(center, vec)
