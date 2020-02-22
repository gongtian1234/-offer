'''
题目：输入一个整型数组，数组里有正数也有负数。数组中一个或连续的多个整数组成一个子数组，求所有子数组和的最大值。
例如，{6,-3,-2,7,-15,1,2,2}, 连续子向量的最大和为8(从第0个开始到第三个为止)。要求时间复杂度为O(n)【题目的意思是找出连续的数字中
那几个加起来是最大的，只需要找到子数组和最大的那个和就行，不需要找出子数组】

思路：
找两个辅助变量，一个记录最大和，另一个记录加到第i个数之前的和，通过遍历数组，从而找到连续子数组的最大和
'''

def findGreatestSumOfArray(array):
    if array==[]:
        return 
    maxSum = None
    preSumI = None
    for i in array:
        if maxSum is None and preSumI is None:
            maxSum = i
            preSumI = 0
        if preSumI+i<i:    # 如果和小于i，则从i开始
            preSumI = i
        else:
            preSumI += i
        if maxSum<preSumI:
            maxSum = preSumI
    return maxSum

if __name__ == '__main__':
    print(findGreatestSumOfArray([1,-2,3,10,-4,7,2,-5]))    # 18
