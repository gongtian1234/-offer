# 题目证明巴德赫猜想。任意大于2的偶数都可以写成两个质数（素数）之和，如16=3+13。（这道题换句话表达：将任意一个大于
# 2的偶数表示为两个质数之和）

'''
思路：
首先，根据上一道题，计算n以内的所有素数个数，可以得到这个偶数范围内的所有素数，而且是排好序的；
其次，有两种方法解题：①用两个for循环，将两个素数加起来，判断其是否等于输入的这个偶数；
②找两个指针，分别指向第一步得到的有序素数列表的头尾记为i、j，如果i、j所指向的数之和大于这个偶数，那么j往左移一位
再次判断；如果i、j所指向的数之和小于这个偶数，那么i往右移一位；如果等于这个偶数，则返回所指的两个质数。
注意：第一种方法的时间复杂度为O(n^2)；第二种方法的时间复杂度为O(n)
'''

def find_sushu(num):
    bool_array = [1 for i in range(num+1)]
    bool_array[0], bool_array[1] = 0, 0
    for tmp in range(2, num+1):
        if bool_array[tmp]==0:
            continue
        beishu = 2
        while 1:
            if tmp*beishu > num:
                break
            if bool_array[tmp*beishu]==0:
                beishu += 1
                continue
            bool_array[tmp*beishu] = 0
            beishu += 1
    sushu_lst = []
    for tmp in range(len(bool_array)):
        if bool_array[tmp]==1:
            sushu_lst.append(tmp)
    return sushu_lst


def solution(num2):
    if num2%2!=0:                   # 判断是否是一个偶数
        return "请输入一个偶数!!!"
    sushu_lst = find_sushu(num2)
    # print(sushu_lst)
    cur1, cur2 = 0, len(sushu_lst)-1  # 两个游标，分别指向素数列表的头和尾
    while 1:
        if cur1>cur2:
            print('没有找到，一定是哪出问题了！')
        sum_cur1_2 = sushu_lst[cur1]+sushu_lst[cur2]
        if sum_cur1_2==num2:
            return sushu_lst[cur1], sushu_lst[cur2]
        elif sum_cur1_2>num2:
            cur2 -= 1               # 两个素数之和大于该偶数，则右边的游标cur2左移一位；
        elif sum_cur1_2<num2:
            cur1 += 1               # 两个素数之和小于该偶数，则左边的游标cur1右移一位

num3 = 15022
print(solution(num3))