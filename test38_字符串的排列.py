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

# leetcode46：这是针对数字的全排列
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        m = len(nums)
        if m<1:
            return []
        elif m==1:
            return [nums]
        rst = []
        for i in range(m):
            j_lst = self.permute(nums[:i]+nums[i+1:])
            for j in j_lst:
                rst.append([nums[i],j])
        r = []
        for i in rst:
            r.append(self.flat(i))
        return r
    def flat(self,nums):
        rst = []
        for i in nums:
            if isinstance(i,list):
                rst.extend(self.flat(i))
            else:
                rst.append(i)
        return rst
