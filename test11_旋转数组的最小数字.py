'''
面试题11：旋转数组中的最小数字。把一个数组最开始的若干元素搬到数组的末尾，则称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素，如[3,4,5,1,2]为[1,2,3,4,5]的旋转，该数组的最小元素为1.

思路：
1、先考虑较为一般的情况，[4,5,6,1,2,3]，找两个游标，分别标在第一个、最后一个元素，再找一个游标标在中间元素，根据旋转数组的本身特点，中间元素与cur1、cur2比较，若大于等于cur1的元素，则将cur1重标在此位置；若小于等于cur2的元素，则将cur2重标在此位置，以此循环缩小范围；
2、在进一步考虑特殊情况：
    1. 把0个元素搬到数组的末尾，这种只要确定cur1的元素小于cur2的元素且cur1的元素不等于mid的元素(为保证该数组的数字不全相同), 则输出cur1；
    2. cur1、cur2、mid指向的元素都相等，此时只能使用顺序查找的方法寻找最小元素【注意：在进入顺序查找进行分析之前，先用set判断一下该数组是否只有一类元素】

'''
class Solution:
    def binary_search(self, alist):
        n = len(alist)
        cur1 = 0
        cur2 = n-1
        mid = n//2

        # 特殊情况1，把0个元素搬到数组的末尾，这种也可称为旋转数组
        if (alist[cur1]<alist[cur2]) and (alist[cur1]!=alist[mid]):
            return cur1

        # 特殊情况2，三个值相等，此时只能使用顺序查找的方法 [1,1,1,1,1]or[1,1,1,0,1]
        if (alist[cur1]==alist[cur2]) and (alist[cur2]==alist[mid]):
            return self.order_search(alist)

        while cur2-cur1>1:
            if alist[mid]>=alist[cur1]:
                cur1 = mid
                mid = (cur1+cur2)//2
            elif alist[mid]<=alist[cur2]:
                cur2 = mid
                mid = (cur1+cur2)//2
        return cur2

    def order_search(self, alist):
        # 进行顺序查找
        cur = 0
        if len(set(alist))==1:
            return cur
        while alist[cur]>=alist[cur+1]:
            cur += 1
        return cur


test = Solution()
# 1、测试递增数组
print(test.binary_search([1,2,3,4,5,6,7])) # 0
# 2、测试一般的旋转数组
print(test.binary_search([4,5,6,7,1,2,3])) # 4
# 3、测试只能用顺序查找的数组
print(test.binary_search([1, 0,1,1,1])) # 1  # 或者是[1,1,1, 0,1]
print(test.binary_search([1,1,1, 0,1])) # 3
print(test.binary_search([1,1,1,1,1])) # 0

