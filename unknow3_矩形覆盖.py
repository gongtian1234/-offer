'''
题目：用2*1的小矩形横着或竖着覆盖更大的矩形，请问用n个2*1的小矩形无重叠的覆盖一个2*n的大矩形，总共有多少种方法

思路：
原理就是斐波那契数列，如果第一块是竖着放的，那么剩下的就相当于n-1的情况，如果第一块是横着放的，那么第二块的方法就确定了，就相当于是n-2的情况


'''

def rectCover(number):
    if number==0:
        return 0
    if number==1:
        return 1
    if number==2:
        return 2
    a = 1
    b = 2
    for i in range(3, number+1):
        # 1 1 2 3 5
        b = a+b
        a = b-a
    return b

print(rectCover(20))