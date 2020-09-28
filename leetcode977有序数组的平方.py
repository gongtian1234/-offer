# leetcode977有序数组的平方
# 输入一个有序数组，要求返回的平方也是有序的，注意处理平方和相同的情况

def sortedSquare(arr):
    if arr is None or len(arr)<1: return arr
    length = arr
    cur2 = 0
    while arr[cur2]<0:  # 用来找到正负数的分界线，cur2指向第一个正数，cur1指向最大的负数（就是离0最近的那个）
        cur2 += 1
    cur1 = cur2-1
    rst = []
    while cur1>=0 and cur2<length:
        left, right = arr[cur1]**2, arr[cur2]**2
        if left<right:
            rst.append(left)
            cur1 -= 1
        elif left>right:
            rst.append(right)
            cur2 += 1
        else:
            rst.append(left)
            while cur1-1>=0 and arr[cur1]==arr[cur1-1]:
                rst.append(left)
                cur1 -= 1
            cur1 -= 1
            rst.append(right)
            while cur2+1<length and arr[cur2]==arr[cur2+1]:
                rst.append(right)
                cur2 += 1
            cur2 += 1
    while cur1>=0:
        rst.append(arr[cur1]**2)
        cur1 -= 1
    while cur2<length:
        rst.append(arr[cur2]**2)
        cur2 += 1
    return rst
    
    
# 变体：返回有序数组中平方和不同的个数
# 思路和上一个差不多，稍微有些变化即可
def numOfSortSquare(arr):
    if arr is None or len(arr)<1: return arr
    rst = 0
    length = len(arr)
    cur2 = 0
    while arr[cur2]<0: cur2 += 1
    cur1 = cur2-1
    while cur1>=0 and cur2<length:
        left, right = arr[cur1]**2, arr[cur2]**2
        if left>right: 
            rst += 1
            cur2 += 1
        elif left<right:
            rst += 1
            cur1 -= 1
        else:
            rst += 1
            while cur1-1>0 and arr[cur1]==arr[cur1-1]:
                cur1 -= 1
            cur1 -= 1
            while cur2+1<length and arr[cur2]==arr[cur2+1]:
                cur2 += 1
            cur2 += 1
    while cur1>=0:
        rst += 1
        while cur1-1>=0 and arr[cur1]==arr[cur1-1]:
            cur1 -= 1
        cur1 -= 1
    while cur2<length:
        rst += 1
        while cur2+1<length and arr[cur2]==arr[cur2+1]:
            cur2 += 1
        cur2 += 1
    
    
    
