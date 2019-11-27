'''
经典二分搜索：
适用条件：①该数组已经排好序；②要找到某个重复数字的第一个或者最后一个数；
在使用前要考虑的情况：①是否排好序；②是否有重复的数；③有没有负数；
'''

def binarysearch(alist, item):   # 可以找到重复数字的第一个
    if len(alist)==0:
        return -1
    left, right = 0, len(alist)-1
    while left+1<right:
        mid = (left + right) // 2
        if alist[mid]==item:
            right = mid
        elif alist[mid]<item:
            left = mid
        elif alist[mid]>item:
            right = mid
    if alist[left]==item:return left
    elif alist[right]==item:return right
    return -1

print(binarysearch([1,1,1,2,2,2,3,3,3,4,5,6], 2))
