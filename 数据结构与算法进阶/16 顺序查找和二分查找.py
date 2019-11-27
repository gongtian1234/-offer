## 顺序查找
def solution(array, k):
    for i in range(len(array)):
        if k==array[i]:
            return True
    return False
print(solution(['a','b','c','e'], 'd'))

## 二分查找
## 注意：二分查找传进去的数组必须是从小到大排好序的
def solution2(array, num):
    if len(array)==0:   # 空数组
        return False
    if num>array[-1] or num<array[0]:   # 查找的元素超出数组的范围[min,max]
        return False
    cur1, cur2 = 0, len(array)-1
    while cur1<=cur2:
        if array[cur1]==num:
            return True
        elif array[cur2]==num:
            return True
        mid = cur1 + (cur2-cur1)//2
        if array[mid]<num:
            cur1 = mid
        elif array[mid]>num:
            cur2 = mid
        elif array[mid]==num:
            return True
print(solution2([1,2,3,4,5],3))
print(solution2([1,1,2,3,3],3))