# matrix(leetcode542): 寻找数组中的每个数距离0最近的步长，自身为0，则所需步长为1，最终返回一个矩阵
# 还有一种使用图论的广度优先搜索的方法，但是图论这一块不会

def updateMatrix(arr):
    if arr is None: return arr
    def DP(i, j, m, n, rst):
        if i>0: rst[i][j] = min(rst[i][j], 1+rst[i-1][j])
        if j>0: rst[i][j] = min(rst[i][j], 1+rst[i][j-1])
        if i<m-1: rst[i][j] = min(rst[i][j], 1+rst[i+1][j])
        if j<n-1: rst[i][j] = min(rst[i][j], 1+rst[i][j+1])
    rst = [[0 if arr[i][j]==0 else float('inf') for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            DP(i,j,m,n,rst)
    for i in range(m):
        for j in range(n):
            DP(i,j,m,n,rst)
    return rst

print(matrix([[0,0,0],[0,1,0],[1,1,1]]))
