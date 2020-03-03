'''
题目：把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率

思路：
动态规划问题。f(n, s) = f(n-1, s-1) + f(n-1, s-2) + f(n-1, s-3) + f(n-1, s-4) + f(n-1, s-5) + f(n-1, s-6)。初始条件，f(1,1)=f(1,2)
=f(1,3)=f(1,5)=f(1,6)=1 
参考网址：https://www.bbsmax.com/A/1O5EVXAWd7/
'''

def printProbility(n):
    if n<1:
        return 
    dp = [[0 for i in range(6*n)] for i in range(n)]    # 相当于是设置出n个骰子，每个骰子都有6n个位置，用来计数，方便下面进行的动态规划
    for i in range(6):                                  # 只有一个骰子时，1-6都只会出现一次
        dp[0][i] = 1
    for i in range(1,n):
        for j in range(i, 6*(i+1)):                     # i表示第几个骰子，当出现第i+1个骰子时，最小和为i*1，最大和为6*(i+1)，i从0开始
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j-2]+dp[i-1][j-3]+dp[i-1][j-4]+dp[i-1][j-5]+dp[i-1][j-6]
    count = dp[n-1]
    sums = sum(count)
    prob = []
    for i in count:
        prob.append(i/sums)
    return prob                                         # 第0个位置表示和为1的概率，第1个位置表示和为2的概率

if __name__ == '__main__':
    print(printProbility(5))

    # 1    2(1) 3(1+1) 4(1+1+1) 5(1+1+1+1) 6(1+1+1+1+1) 7(1+1+1+1+1+1) 8(1+1+1+1+1) 9(1+1+1+1) 10(1+1+1) 11(1+1) 12(1)
       # 1 2 3 4 5 6 5 4 3 2 1