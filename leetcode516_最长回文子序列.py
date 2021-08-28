# leetcode516: 最长回文子序列(这里的回文子序列可以不连续)
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
        
def solution(s):
    # leetcode5:最长回文子串
    m = len(s)
    if m<1:
        return 0
    elif m==1:
        return 1
    arr = [[0]*m for _ in range(m)]
    tmp_rst = ''  # 存储最长回文子串
    for i in range(m):
        arr[i][i] = 1
    max_length = 1
    for i in range(m-1):
        if s[i]==s[i+1]:
            arr[i][i+1] = 1
            max_length = 2
            tmp_rst = s[i:i+2]
    for length in range(2,m,1):  # length表示的是首尾字符的间隔长度
        for i in range(m-length):
            j = i + length
            if arr[i+1][j-1]==1 and s[i]==s[j]:
                arr[i][j] = 1
                max_length = length + 1
                tmp_rst = s[i:j+1]
    # for i in range(m):
    #     print(arr[i])
    print(tmp_rst)
    return max_length
