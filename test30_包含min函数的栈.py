'''
题目：定义栈的数据结构，在栈的原有功能上添加一个能够得到栈的最小元素的min函数，要求：在该栈中，调用min、push及pop的时间复杂度都是O(1)

思路：
①栈的特点是先进后出，后进先出。栈的功能主要有：push（进栈）、pop（出栈）、top（栈顶元素）；
②遍历栈去寻找元素，时间复杂度为O(n)，题中要求是O(1)，所以考虑用空间换时间，创建一个存放最小值的列表，在每次进栈时都比较，对应放入最小值，
从而栈有多长（假设为n），则最小元素的列表也为n

'''
class Solution(object):
    def __init__(self):
        self.stack = []
        self.minValue = []

    def push(self, node):
        self.stack.append(node)
        if len(self.minValue)==0:
            self.minValue.append(node)
        else:
            if self.minValue[-1]<node:
                self.minValue.append(self.minValue[-1])
            else:
                self.minValue.append(node)

    def pop(self):
        if len(self.stack)==0:
            return 
        self.minValue.pop()
        return self.stack.pop()

    def top(self):
        if len(self.stack)==0:
            return 
        return self.stack[-1]
        
    def min(self):
        return self.minValue[-1]


s = Solution()
s.push(4)
s.push(3)
s.push(6)
s.push(9)
print(s.min())    # 3
print(s.minValue) # [4, 3, 3, 3]
print(s.pop())    # 9
print(s.minValue) # [4, 3, 3]
