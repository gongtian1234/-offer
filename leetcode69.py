# leetcode69实现sqrt函数（lletcode原题）
# 使用二分法解决问题，当num小于1时，设置end为1
def mySqrt(num):
    if num<0:
        return -1
    left, right = 0, num
    if num<1:
        right = 1
    while left<=right:
        mid = (left + right) / 2
        if abs(mid**2 - num)<=0.001:
            return mid
        elif (mid**2 - num)>0.001:
            right = mid
        elif -(mid**2 - num)>0.001:
            left = mid
    return mid