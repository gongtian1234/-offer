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
    
# 礼物的最大价值及其路径
## 思路：前半部分一样，先是根据动态规划的方法找到礼物的最大价值矩阵，然后再根据这个矩阵反向找到取得最大价值时的路径
def maxValueAndPath(rows, columns, lst):
    if lst is None or rows*columns!=len(lst): return 
    arr = [[0]*(columns+1) for _ in range(rows+1)]
    for i in range range(rows+1):
        for j in range(columns+1):
            if i==0 or j==0: arr[i][j] = 0
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1]) + lst[(i-1)*columns+j-1]
    max_value = arr[rows][cloumns]
    path = []
    if rows==1 or columns==1: path = lst
    else:
        path.append(lst[-1])
        i, j = rows, columns
        while i>1 and j>1:
            if arr[i-1][j]>arr[i][j-1]: 
                path.append(lst[(i-1)*columns - (columns-j) -1])
                i = i -1
            else:
                path.append(lst[(i-1)*columns + (j-1) - 1])
                j -= 1
        path.append(lst[0])
        path = path[::-1]
    return path, max_value
                
        
