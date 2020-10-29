'''
输入一个倒Z字形的字符串和行数rows，输出其一行一行遍历时的字符串

思路（参考文章Leetcode6: ZigZag Conversion:https://blog.csdn.net/bestallen/article/details/53081100）：

首先分为两部分进行处理，第一部分是处理垂直线上的元素，可以发现每一行上垂直线的元素下标索引相差，以第0行为例，索引0的下一个元素为，再下一个元素对应，以此类推（在字符串的长度内）；
第二部分就是定位斜线上的元素，斜线上的元素索引对应公式为，其中j为第i行垂直线上的元素索引；
最后再单独处理最后一行的元素
'''

class Solution(object):
    def convert(self, s, numRows):
        if len(s)<numRows or numRows==1: return s
        length = len(s)
        step = 2*numRows -2
        rst = s[::step]                    # 首行和尾行需要单独处理
        for i in range(1,numRows-1,1):
            for j in range(i,length,step):
                rst += s[j]                # 处理垂直线上的元素
                if j+(step-2*i)<length:    # 处理斜线上的元素
                    rst += s[j+(step-2*i)]
        rst += s[numRows-1::step]
        return rst
