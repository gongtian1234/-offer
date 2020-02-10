'''
题目15：二进制中1的个数。实现一个函数，输入一个整数，输出该数二进制中1的个数。如9的二进制为1001，有2位是1，因此返回2。

注：Python中没法做，用书上的左移解题时，python中并不会说到64/32结束，会一直左移下去，那么这个数就会一直变大；关键是负数
    不好处理，牛客网的题中标明负数用补码表示，也有网友给出了2**32+n(n<0时)(可以转为补码)，但是这是针对32位计算机的，64位的就是64，而且
    当这个数非常大时，加2**32还是负数，此时就不再适用了；我在写出的demo为负数还是统计原码中1的个数，针对补码时就不对了

'''

class Solution:
    def NumberOf1(self, number):
        flag = 1
        count = 0
        stp = 0
        abs_number = number if number>=0 else -number 
        while flag<=abs_number:
            if number&flag:    # 按位与运算，把两个数都转换为二进制，然后比较对应位置的数是否相同，相同为1，否则为0，最后返回十进制数
                count += 1
            flag = flag<<1
        return count


test = Solution()
print('hello')
print(test.NumberOf1(1))
print(test.NumberOf1(-2147483648))
print(test.NumberOf1(-1))     # 牛客上的答案为32，这里计算得到的答案为1
print(test.NumberOf1(100))

# return bin(n).replace("0b","").count("1") if n>=0 else bin(2**32+n).replace("0b","").count("1")    # 这个处理绝对值大于2**32的负数时有问题

'''
&: ①与运算；②按位与运算，(一个数&1)的结果就是取二进制的最末位。参考网址：https://zhidao.baidu.com/question/146401227.html
<<: 是按位左移，如3，二进制表示为0000 0011，3<<1(左移1位)：变为0000 0110，十进制数为6；
>>: 按位右移，比左移复杂一点，因为右移需要判断符号，若为负，右移时补1，若为正，右移时补0； 
'''

'''
new method
=====================================================================================================================
题目：实现一个函数，输入一个整数，输出该数二进制中1的个数。如9的二进制为1001，有2位是1，因此返回2。(其中负数用补码表示)

思路：
python比较特殊，不管数有多大都不会溢出，所以在此只取前32位(n = 0xFFFFFFFF&n 一个F是4个1)
①将截取的32位数字转换为二进制，再转换为字符串统计1的个数；
②将数字左移统计；
③在while中n=n&(n-1),count+=1, 每次n&(n-1)都会减去二进制中的一个1
'''

def numOf1(n):
    ''' 方法一 '''
    # n = 0xFFFFFFFF & n
    # count = 0
    # for i in str(bin(n)):
    #     if i == '1':
    #         count += 1
    # return count

    ''' 方法二 '''
    # count = 0
    # for i in range(32):
    #     mask = 1<<i    # mask每次左移一位去判断n的第n位是不是1
    #     if n & mask !=0:
    #         count += 1
    # return count    

    ''' 方法三 '''
    count = 0
    while n:
        n = n&(n-1)
        count += 1
        n = 0xFFFFFFFF&n
    return count
print(numOf1(-2147483648))
