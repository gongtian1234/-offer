'''
题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有顺序都不相等。例如1,2,3,4,5
是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,2,1就不可能是该压栈序列的弹出序列。

思路：
每压入一个元素，都会考虑弹出或不弹出的情况，不弹出则继续压入；弹出则弹出，下一个元素接着考虑是否弹出，不弹出则压入，由此得到第二个序列，
即第二个序列是出栈方式中的一种可能结果
'''
class Solution(object):
    def IsPopOrder(self, pushV, popV):
        if len(pushV)==0 or len(pushV)!=len(popV):    # 边缘检测
            return 
        stack = []
        index = 0
        for item in pushV:
            stack.append(item)
            while len(stack)>0 and stack[-1]==popV[index]:
                stack.pop()
                index += 1
        return True if len(stack)==0 else False

print(Solution().IsPopOrder([1,2,3,4,5,6], [4,3,5,6,2,1]))
