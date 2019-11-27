'''
题目：给定有序数组和一个目标值，如果在数组中找到此目标值则返回与目标值相等的值的index，如果没有找到，则返回目标值按顺序应该被插入的位置。
     （住：假设该数组中不存在重复数）

思路：有点类似于插入排序。
实际上就是找到第一个大于等于item的数的位置，没有找到则放在最后的位置上

'''
def find_insert_position(array, item):
    if len(array)==0:return -1
    cur1, cur2 = 0, len(array)-1
    while cur2-1>cur1:
        mid = (cur1+cur2)//2
        if array[mid]==item:return mid
        if array[mid]>item:
            cur2 = mid
        else:
            cur1 = mid
    if array[cur1]>=item:return cur1
    if array[cur2]>=item:return cur2
    return cur2+1
print(find_insert_position([1,3,5,7,9,11],2))
