'''
输入一个正或负的整数，输出其颠倒后的整数，如果溢出则返回0（溢出：小于或大于）
思路：

第一种方法：先判断是否有负号，然后将去掉负号的字符串倒序过来([::-1])，再判断是否越界
第二种方法：倒序遍历至索引1的位置（在遍历的过程中每次都检验是否越界，越界则直接返回0），最后单独判断索引0位置
'''
class Solution(object):
    def reverse(self, x):
        # 第二种方法
        downLimit, upLimit = -2**31, 2**31-1
        rst = ''
        xStr = str(x)
        length = len(xStr)
        for i in range(length-1, 0, -1):
            if len(rst)>0 and int(rst)>upLimit: return 0
            rst += xStr[i]
        if xStr[0]=='-':
            return -1*int(rst) if -1*int(rst)>=downLimit else 0
        else:
            rst += xStr[0]
            return int(rst) if int(rst)<=upLimit else 0
        
        # 第一种方法
        xStr = str(x)
        if xStr[0]=='-':
            xSrt = xStr[1:][::-1]
            return -1*int(xStr) if -1*int(xStr)>=-2**31 else 0
        else:
            xSrt = xStr[1:][::-1]
            return int(xStr) if int(xStr)<=2**31-1 else 0
        
