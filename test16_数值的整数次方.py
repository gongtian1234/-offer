'''
题目：数值的整数次方。求base值得整数次方，不得使用库函数，同时不用考虑最大数的问题

思路：①要考虑全面。有正整数次方，也有0和负整数次方，正整数直接相乘即可，0直接返回1，负整数在正数的基础上取倒数
      ②方法一，直接使用循环e个数相乘解题，但是时间复杂度较高
      ③方法二，用递归解题逐层递归自上而下，时间复杂度好像第一点, 当n为偶数时，a^{n}=a^{n/2}a^{n/2}a, 当n为奇数时，a^{n}=a^{(n-1/2)}a^{(n-1/2)}a,
      例如，若 exponent 为 32，按照上面 power 函数的做法，for 循环中要进行31次乘法。若是换一种思路思考：base^{32}等于base^{16}的二次方，
      base^{16}又是base^{8}的二次方。以此类推，做32次方只需5次乘法，先求2次方，然后4次方, 然后8次方，再然后16次方，最终求得32次方。
      原文链接：https://blog.csdn.net/Breathing_yang/article/details/94298167


'''


import os

def solution1(base,exp):
    '''方法一使用for循环解题'''
    if base==0:return 0
    if exp==0 or base==1:
        return 1
    elif exp>0:
        tmp = 1
        for i in range(exp):
            tmp = tmp * base
        return tmp
    else:
        tmp = 1
        for i in range(-exp):
            tmp = tmp * base
        return 1 / tmp

# 测试用例：正数、9负数次方
print(solution1(1, 0))
print(solution1(10, 5))
print(solution1(10, -10))
print(solution1(0, 5))

def solution2(base, exp):
    '''方法二：使用递归的方式'''
    if base==0:return 0

    if exp==0:
        return 1
    elif exp==1:
        return base
    elif exp==-1:
        return 1/base

    result = solution2(base, exp>>1)
    result *= result
    if (exp & 0x1)==1:
        result *= base
    return result

# 测试用例：正数、9负数次方
print(solution2(1, 0))
print(solution2(10, 5))
print(solution2(10, -5))
print(solution2(0, 5))


os.system('pause')
