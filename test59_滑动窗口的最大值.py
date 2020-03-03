'''
题目一：滑动窗口的最大值。给定一个数组和滑动窗口，请找出所有滑动窗口的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
那么一个存在6个滑动窗口，它们的最大值分别为{4,4,6,6,6,5}

思路：
①每次选取k个数里面最大的，但是这样的时间复杂度大，为O(n^2)
②双向队列，时间复杂度为O(n)。遍历整个数组，先删除超出窗口数的索引；再删除小于numbers[i]的数的索引；从第k-1个索引开始添加

题目二：队列的最大值。请定义一个队列并实现函数max得到队列里的最大值。要求函数max、push_back、pop_front的时间复杂度都是O(1)

思路：
'''

def maxInWindows(numbers, k):
    if numbers is None or len(numbers)<k or k<1:
        return []
    doubleQueue, rst = [], []
    for i in range(len(numbers)):
        if len(doubleQueue)>0 and i-k+1>doubleQueue[0]:                      # 删除超出窗口的数的索引
            doubleQueue.pop(0)
        while len(doubleQueue)>0 and numbers[doubleQueue[-1]]<=numbers[i]:    # 删除小于numbers[i]的数的索引
            doubleQueue.pop()
        doubleQueue.append(i)
        if i>=k-1:                                                           # 从第k-1个索引出开始添加
            rst.append(numbers[doubleQueue[0]])
    return rst

if __name__ == '__main__':
    print(maxInWindows([2,3,4,2,6,2,5,1],3))