"""
    Author: Dell
    Time: 2019/10/18 10:32
"""

if __name__ == '__main__':
    file1 = open("./hightf-idf.txt", 'r', encoding='UTF-8')
    file2 = open("./vectors.txt", 'r', encoding='UTF-8')
    names, datas = [], []
    for name in file1.readlines():
        names.append(name.strip())
    for data in file2.readlines():
        datas.append(data.split())
    with open("./Rebuilt.txt", 'w+') as f:
        for name in names:
            for data in datas:
                if name == data[0]:
                    f.write(' '.join(data) + '\n')
