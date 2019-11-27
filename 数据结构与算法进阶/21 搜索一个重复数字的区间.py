'''
题目：搜索一个区间。给定一个排好序的有重复数字的array，找到一个给定目标值的起始位置和结束位置。如果都没有，返回(-2,-2)

思路：
就是先找到第一次出现的位置，再找到第二次出现的位置。【用的是18中的经典二分搜索的方法】
这种解法的时间复杂度为log(n)+log(n),用for从头到尾遍历的时间复杂度为O(n)
'''

def find_1st_position(array, item):
    if len(array)==0:return -1
    cur1, cur2 = 0, len(array)-1
    while cur2-1>cur1:
        mid = (cur1+cur2)//2
        # if array[mid]==item:return mid
        if array[mid]<item:
            cur1 = mid 
        else:
            cur2=mid
    if array[cur1]==item:return cur1
    if array[cur2]==item:return cur2
    return -2
def find_last_position(array, item):
    if len(array)==0:return -1
    cur1, cur2 = 0, len(array)-1
    while cur2-1>cur1:
        mid = (cur1+cur2)//2
        # if array[mid]==item:return mid
        if array[mid]<=item:
            cur1 = mid 
        else:
            cur2=mid
    if array[cur1]==item:return cur1
    if array[cur2]==item:return cur2
    return -2
# print(find_last_position([1,1,1,2,2,2,3,3,3], 2))
# print(find_last_position([1,1,2,2,3,3,3,5], 3))

def find_range(array, item):
    tmp1 = find_1st_position(array, item)
    tmp2 = find_last_position(array, item)
    return (tmp1, tmp2)
print(find_range([1,1,2,2,3,3,3,5], 5))

