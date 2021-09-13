def solution(nums):
    m = len(nums)
    if m<1:
        return 0
    elif m==1 or m==2:
        return max(nums)
    rst = []
    tmp = [nums[i+1]-nums[i] for i in range(m-1)]
    cur1 = 0
    while cur1<len(tmp):
        if tmp[cur1]>0:
            tmp_sum = []  # 存储连续的正数
            tmp_sum.append(tmp[cur1])
            cur1 += 1
            while cur1<len(tmp) and tmp[cur1]>0:
                tmp_sum.append(tmp[cur1])
                cur1 += 1
            rst.append(sum(tmp_sum))
        else:
            cur1 += 1
    return sum(sorted(rst)[-2:])
print(solution([1,2,3,4,5]))
print(solution([3,3,5,0,0,3,1,4]))
print(solution([7,6,4,3,1]))
print(solution([2,2,3,4,3]))
