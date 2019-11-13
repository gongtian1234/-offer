'''
扫雷游戏。程序接收三个参数M,N,p，然后生成一个M*N的矩阵每一个cell都有p的概率是地雷，生成矩阵后，然后再计算每一个cell周围
地雷的数量。
思路：难度2星。因为边界的判断是个问题，在边上的格子只有5个邻居，在角上的格子只有三个邻居，只有在内部的才有八个邻居，可以
      直接写程序，但是这样有些太麻烦。所以应用了一个小技巧，在边界加上一层框，即行数和列数各增加2行/列，且和真正棋盘上的
      元素都不一样，用以区分。
      首先，先创建一个棋盘；
      然后再依次挨个遍历；
'''

import random
def minesweeper(m, n, p):
    # 先画一张棋盘
    qipan = [[None]*(n+2) for i in range(m+2)]
    # 利用随机数生成地雷
    for row in range(1, m+1):
        for col in range(1, n+1):
            r = random.random()
            qipan[row][col] = -1 if r<p else 0
    # 依次遍历m*n的表，标出每个框周围雷的个数
    for row in range(1, m+1):
        for col in range(1, n+1):
            tmp = qipan[row][col]
            if tmp==-1:
                continue
            # 依次遍历每个该元素的上下两行和上下两列的相邻元素
            for rowi in range(row-1, row+2):
                for coli in range(col-1, col+2):
                    if rowi==row and coli==col:
                        continue
                    tmpi = qipan[rowi][coli]
                    # print('{} {}:{}'.format(rowi, coli, tmpi))
                    if tmpi==-1:
                        qipan[row][col] += 1
    for i in range(1,len(qipan)-1):
        print(qipan[i][1:-1])
    # 如果为了结果更加美观可以直接转为DataFrame
minesweeper(20,20,0.2)

