'''
题目：把因子只包含2、3、5的称为丑数(ugly number)。求按从小到大第N个丑数，例如6、8都是丑数，但是14不是，因为它的因子包含7，习惯上把1当做
第一个丑数（注意：主要考虑时间复杂度）

思路：
①（暴力方法）从1一直判断下去，知道找到第N个丑数（判断丑数的方法：先无限整除2，再无限整除3，最后再无限整除5，如果最终得到1则就是丑数，否则不是）
②找3个指针，分别表示*2、*3、*5，都从1开始，判断大小找到小的数存放起来，并且对应的指针往前移一位，如1  *2、*3、*5，对应的最小的数为2，则将2
添加到列表里，并将*2的指针往前移动一位，依次类推，知道找到第N个丑数为止
'''

def getUglyNumber(n):
    if n<1:
        return 0

    twoPointer = 0    # two\threee\five Pointer指的是索引
    threePointer = 0
    fivePointer = 0
    uglyList = [1]
    count = 1
    while count!=n:
        minValue = min(2*uglyList[twoPointer], 3*uglyList[threePointer], 5*uglyList[fivePointer])
        uglyList.append(minValue)
        count += 1

        if minValue==2*uglyList[twoPointer]:
            twoPointer += 1
        if minValue==3*uglyList[threePointer]:
            threePointer += 1
        if minValue==5*uglyList[fivePointer]:
            fivePointer += 1
    return uglyList[count-1]

print('第200个丑数为',getUglyNumber(200))    # 16200



