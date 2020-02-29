'''
题目：输入一个字符串，打印出该字符串中字符的所有排列。例如，字符串a、b、c所能排列出的所有字符串有abc、acb、bac、bca、cab和cba

思路：
看不懂,死记吧
'''
class Solution:
    def permutation(self,s):
        if len(s) == 0:
            return []
        if len(s) <= 1:
            return s
        sl = []
        for i in range(len(s)):
            for j in self.permutation(s[0:i] + s[i + 1:]):
                sl.append(s[i] + j)
        return sorted(list(set(sl)))

s = Solution()
print(s.permutation(['a','b','c']))
