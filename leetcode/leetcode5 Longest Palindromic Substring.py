'''
最长回文子序列，这里指的是连续的子序列字符（区别于leetcode516：允许字符串不连续，并且只要找到长度即可）
思路：不会，参考https://blog.csdn.net/asd136912/article/details/78987624
     或者暴力解题，但是会超时
'''
# 暴力解题:这种方法可以做，但是会超时152/176
class Solution(object):
    def longestPalindrome(self, s):
        if s is None or len(s)<1:
            return
        elif len(s)==1: return s
        length = len(s)
        rst = s[0]
        for i in range(length):
            for j in range(i+1,length,1):
                tmp_rst = s[i:j+1]
                if s[i]==s[j] and j-i+1>len(rst):
                    cur1,cur2 = i,j
                    sign = 1
                    while cur1<cur2:
                        if s[cur1]!=s[cur2]:
                            sign = 0
                            break
                        cur1+=1; cur2-=1
                    if sign and len(tmp_rst)>len(rst):
                        rst = tmp_rst
        return rst

# 方法二：没看明白
class Solution(object):
    def longestPalindrome(self, s):
        if s is None or len(s)<1:
            return
        elif len(s)==1: return s
        m = length(s)
        max_len, start = 0, 0
        for i in range(m):
            if i-max_len>=1 and s[i-max_len-1:i+1]==s[i-max_len-1:i+1][::-1]:
                start = i-max_len-1
                max_len += 2
                continue
            if i-max_len>=0 and s[i-max_len:i+1]==s[i-max_len:i+1]:
                start = i-max_len
                max_len += 1
        return s[start:start+max_len]
