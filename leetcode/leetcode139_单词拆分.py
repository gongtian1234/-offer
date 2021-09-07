# https://leetcode-cn.com/problems/word-break/solution/139-dan-ci-chai-fen-dong-tai-gui-hua-pyt-u6b4/
# 参考文章：https://blog.csdn.net/zhang_han666/article/details/111184525, dp[i]表示s[0:i]的字符串是否可拆分
def wordBreak(s, wordDict):
  n = len(s)
  dp = [True] +[False]*n
  for i in range(n):
    for j in range(i+1,n+1):
      if dp[i]==True and s[i:j] in wordDict:
        dp[j] = True
  return dp[-1]
