'''
题目：输入数字n，按顺序打印出从1到最大的n位十进制数。如输入3，，则打印出1,2,3,...,999

思路：关键在于怎么设置循环结束的条件（在其他语言中要考虑大数，防止溢出，但是在python中不用考虑溢出的问题）
'''

import os

def print1ToMaxOfNDigits_1(n):
    if n<=0:
        return

    stpnum = int('9'*n)
    for i in range (1, stpnum+1):
        print(i, end=' ')
print1ToMaxOfNDigits_1(0)

os.system('pause')