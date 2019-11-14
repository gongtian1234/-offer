'''
题目：反转字符串
思路（这个题目还是很简单的）：
1、直接str[::-1];
2、自己手写一个，也很简单，从第0个位置遍历到第n/2个位置[注意：string是一个不可变的数据类型]

'''

#### 方法1 ####
def reverse1(string):
    string = string[::-1]
    print('reverse1 :{}'.format(string))

#### 方法3 ####
def reverse3(string):
    string = list(string)
    for i in range(len(string)//2):
        string[i], string[len(string)-1-i] = string[len(string)-1-i], string[i]
    print('reverse3 :{}'.format(''.join(string)))

reverse1('hello world')
reverse3('are you sure?')

import os
os.system('pause')