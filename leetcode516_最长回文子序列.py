# leetcode516: 最长回文子序列
# 也是动态规划的思路，先列出转移方程，再解决问题
# d[i][j]表示s[i]……s[j]间的最长回文子序列数量，当i=j是,d[i][j]=1;
# 当i不等于j时，d[i][j]=max{d[i+1][j], d[i][j-1]}
# 相关题目：最长公共子序列

def longestPalindromeSubseq(s):
    length = len(s)
    if length<1:return 0
    elif length==1: return 1
    m = length
    rst = [[0]*m for _ in range(m)]
    for i in range(m): rst[i][i] = 1
    for i in range(m-1, -1, -1):
        for j in range(i+1, m, 1):
            if s[i]==s[j]:
                rst[i][j] = 2 + rst[i+1][j-1]
            else:
                rst[i][j] = max(rst[i+1][j], rst[i][j-1])
    return rst[0][m-1]
        
