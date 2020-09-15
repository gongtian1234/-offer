# 最长公共子序列（这个子序列是可以不连续的，但是是有先后顺序的）
# 动态规划问题，leetcode1143题，array[i][j]表示s1序列的前i个元素、s2序列的前j个序列的公共子序列数，
# 当i=0或j=0时，array[i][j]=0；
# 当x_i=y_j时，array[i][j]=array[i-1][j-1]+1；
# 当x_i不等于y_j时，array[i][j]=max(array[i-1][j],array[i][j-1])

def longestCommomSeries(s1, s2):
    if len(s1)==0 or len(s2)==0:
        return 0
    length1, length2 = len(s1), len(s2)
    array = [[0]*(length2+1) for _ in range(length1+1)]
    result = 0
    for i in range(length1+1):
        for j in range(length2+1):
            if i==0 or j==0:
                array[i][j] = 0
            elif s1[i-1]==s2[j-1]:
                array[i][j] = array[i-1][j-1] + 1
                result = max(result, array[i][j])
            else:
                array[i][j] = max(array[i-1][j], array[i][j-1])
    return result