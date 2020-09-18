# 先对arr进行排序，找三个指针来处理，cur1是跟着for循环更新；cur2、cur3是在里面动态移动
# 但是这样无法通过leetcode上的全部测试，会时间超时

def threeSum(arr, target_sum=0):
    length = len(arr)
    if length<=2:
        return []
    rst = []
    arr.sort()
    for i in range(length-2):
        cur1 = i
        cur2 = i + 1
        cur3 = length-1
        while cur2<cur3:
            three_sum = arr[cur1] + arr[cur2] + arr[cur3]
            if three_sum>target_sum:
                cur3 -= 1
            elif three_sum<target_sum:
                cur2 += 1
            elif three_sum==target_sum:
                rst.append([arr[cur1], arr[cur2], arr[cur3]])
                while cur3-1>cur2 and arr[cur3]==arr[cur3-1]:
                    rst.append([arr[cur1], arr[cur2], arr[cur3]])
                    cur3 -= 1
                cur2 += 1
                cur3 -= 1
    return (rst)
