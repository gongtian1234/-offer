'''
递归的题目：求和、阶乘、斐波那契数列（时间复杂度为2^n）
注意：在递归里面仍然会把整个函数执行一遍，自下而上
思路：
1、普通的递归方式，时间复杂度为O(2^n)，n=40时，直接执行不了；
2、用for循环，每次把上一次的结果放入列表中，下一次计算时直接用列表中寻找上一次的结果；
3、找两个临时变量存储上两次的值用于计算下一次的结果，这样可用for，也可以用递归；
'''

def fibonacci3(n):
    assert n>=0
    if n<=1:
        return (n,0)
    (n1, n2) = fibonacci3(n-1)   # n1是n-1，n2是n-2
    return (n1+n2, n1)
print(fibonacci3(5))

def fibonacci1(n):
    assert n>=0
    if n<=2:
        return 1
    return fibonacci1(n-1) + fibonacci1(n-2)

print(fibonacci1(5))

