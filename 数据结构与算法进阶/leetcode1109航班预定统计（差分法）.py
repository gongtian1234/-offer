# 题目链接：https://leetcode-cn.com/problems/corporate-flight-bookings/
def solution(bookings,n):
    rst = [0]*n
    for start,end,num in bookings:
        rst[start-1] += num  # 好比是在开始站上来num个人
        if end<n:
            rst[end] -= num   # 但是在end站下去了num个人
    return list(accumulate(rst))
