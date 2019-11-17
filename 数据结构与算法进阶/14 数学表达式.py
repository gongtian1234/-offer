'''
题目：数学表达式。给定a和b两个数，a<=b，把b以a乘2或者加1的最快的方式表示出来。
思路：主要分析b>2a以及b%2=0是否成立, 当b<2a时，只能通过加1达到b，当b为奇数时通过加减1使b变为偶数
'''

def solution(a, b):
    # 先设置一个base，即迭代的结束条件
    if a==b:
        return str(a)
    if b<2*a:
        return '(' + solution(a, b-1) + '+1)'
    if b%2==1:
        return '(' + solution(a, b-1) + '+1)'
    # 如果上述条件都不满足，说明b是一个大于2a的偶数
    return solution(a, b/2) + '*2'

print(solution(5,1010))