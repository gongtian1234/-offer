# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers):
        # write code here
        dict = {}
        i = 0
        for num in numbers:
            dict[num] = dict.get(num, 0) + 1    # 字典的get方法，返回指定键的值，不存在则创建默认值
        return dict


aa = Solution()
print(aa.duplicate([12,12,45,65,32,12,45,98,78,98]))

'''
书上的太繁琐，所以字典利用Python的字典优势，直接计数；
如果调包的话，可以使用collection进行计数，不能被局限住。
（这道题的方法非常多，但要结合编程语言的优势来答题更好）
'''

