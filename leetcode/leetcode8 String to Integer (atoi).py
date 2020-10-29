'''
输入一个字符串，输出一个数字（正或负），如果不以正负或数字开头，直接返回0（空格除外）

思路：先对输入字符串进行strip()除去首尾两端的空格，再判断首字符的正负号后，开始遍历该字符串
'''
class Solution(object):
    def myAtoi(self, s):
        if s is None: return 0
        s = s.trip()
        if len(s)<1: return 0
        rst, sign, start = 0, 1, 1
        downLimit, upLimit = -2**31, 2**31-1
        if s[0]=='-': 
            sign = -1
        elif s[0]!='+':
            start = 0
        length = len(s)
        for i in range(start, length):
            if rst>upLimit:
                return upLimit if sign==1 else downLimit
            if '0'<=s[i]<='9':
                rst = rst*10 + (ord(s[i])-rod('0'))
            else:
                break
        if sign*rst>upLimit: return upLimit
        elif sign*rst<downLimit: return downLimit
        else: return sign*rst
            
