'''
题目：输入一个正整数n，求从1到n这n个整数的十进制表示中1出现的次数。例如输入12，从1到12这些整数中包含1的数字有1，10，11和12，1一共出现了5次
（这道题主要是考察时间复杂度）

思路：
①（暴力方法）每个数遍历并去判断其是否含有1
②从个位、十位、百位到最高位，依次判断该位数字为1时可能出现的情况，再将其相加就得到了最终结果
'''

def numOf1Between1AndN(n):
    if type(n)!=int or n<1:
        return None
    cur = 1         # 用来标记当前移动到哪一位，个位（为1）还是百位（为100）等等
    highValue = 1   # 存储当前位右边的数字
    midValue = 1    # 存储当前位上的值
    lowValue = 1    # 存储当前位左边的数字
    sumNumOf1 = 0
    count = 0       # 用来标记当前移动到哪一位，个位（为0）还是百位（为2）、十位(为1)等等

    while highValue!=0:
        # 分别抽取当前位左边、当前位、当前位右边的数字
        highValue = n // (10*cur)
        midValue = n // (cur) % 10
        lowValue = n % cur
        cur = cur*10

        if midValue<1:
            num = (highValue-1+1)*(10**count)
            # 如果当前位小于1，则需要向前一位借1，当前位左边：所以减1，但是从0到highValue共有highValue加1个数
            # 当前位右边：共有10^count种可能性
        elif midValue>1:
            num = (highValue+1)*(10**count)
            # 如果当前位大于1，则不需要向前面借1，因为它可以自由的为1
        else:   # 当前位为1
            # num = highValue*(10**count) + lowValue + 1
            num = (highValue+1)*(lowValue+1) + (highValue-1+1)*(cur-1-lowValue)
            # 如果当前位为1，分两种情况讨论：向前一位不借1或者是借1两种，如523125，当前位为1时，不借1左边只有25+1种，借1后有74种
            # 不借1：右边有(highValue+1)种可能性，左边有lowValue+1种可能性，所以有(highValue+1)*(lowValue+1)种情况
            # 借1：

        sumNumOf1 += num
        count += 1
    return sumNumOf1

print(numOf1Between1AndN(120))