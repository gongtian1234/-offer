'''
题目：在一个m*n的棋盘的每一格都放一个礼物，每个礼物都有一定的价值（价值大于0）.你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下
移动一格，直到到达棋盘的右下角。给定一个棋盘及其上面的礼物，请计算你最多拿到多少价值的礼物

思路：
动态规划。（看不明白，还是看代码死记）
参考网址：https://www.jianshu.com/p/71bc21981090
'''
def getMaxValue(values, rows, cols):
    if len(values)<0 or rows<0 or cols<0:
        return 0
    tmp = [0] * cols
    for i in range(rows):
        for j in range(cols):
            up = 0
            left = 0
            if i>0:
                up = tmp[j]
            if j>0:
                left = tmp[j-1]
            tmp[j] = max(up, left) + values[i*cols+j]
    return tmp[-1]

if __name__ == '__main__':
    print(getMaxValue([7,8,9,4,5,6,1,2,3], 3, 3))