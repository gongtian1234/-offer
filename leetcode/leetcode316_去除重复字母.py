# 题目路径：https://leetcode-cn.com/problems/remove-duplicate-letters/
# 参考网址：https://leetcode-cn.com/problems/remove-duplicate-letters/solution/python3-dan-diao-zhan-316-by-lionking865-lcel/
class Solution:
    def removeDuplicateLetters(self, s):
        stack = []
        dic = {}
        for i in s:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] += 1
        for i in range(len(s)):
            if s[i] not in stack:
                while len(stack)>0 and stack[-1]>s[i] and dic[stack[-1]]>0:
                    stack.pop()
                stack.append(s[i])
            dic[s[i]] -= 1
        return ''.join(stack)
