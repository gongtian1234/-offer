'''
面试题14：剪绳子。给你一根长度为n的绳子，请把绳子剪成m段(m、n都是整数，m、n>1, 【可知：m的取值范围为大于等于2，小于等于n】)，
          每段绳子的长度记为k[0]、k[1]、k[2]、...、k[m]。请问k[0]*k[1]*k[2]*...*k[m]的最大乘积是多少？例如当绳子的长度为8时，
          可以剪长度为为2、3、3的三段，此时得到的最大乘积为18。

思路：两种方法。①用动态规划的方法，自下而上的解题(也可以用递归的方式自上而下解题)，关键在于li的定义及其存放的元素的定义(li里
      的第i个元素指长度为i时的最大乘积，其中0,1,2,3给出的是剪0刀时的最优解)，循环中的i表示当前绳子的长度，j表示剪一刀下去，其
      中一段的长度，则i-j表示另一端的长度；②用贪婪算法进行解题。

难点：要能把一个具体的场景抽象成一个能用动态规划或贪婪算法解决的模型，具体参考书中6.4节。
'''

class Solution:
    def cutRope(self, length):
        ## li[j]表示长度为j时的最优解 ##
        ## 【注意：length=3时，最优解为1，但是当剪绳子剪出3(即j=3)时，最优解为3，因为此时可以不剪】 ##
        li = [0,1,2,3]    # （不必须剪绳子时的，必须捡的情况当做特殊情况在下面进行了讨论）最终列表li会存下所有length对应的最优解，如length=8, 有li: [0, 1, 2, 3, 4, 6, 9, 12, 18]

        if length<2:
            return 0
        if length==2:
            return 1
        if length==3:
            return 2

        temp = 0
        # 自下而上的解题，i表示当前绳子的长度
        for i in range(4, length+1):
            max = 0

            # 这个主要是为了使运算量减半，如i=4,下面的j会从j=1遍历到4，但是j=1与j=3的情况一样，就是j关于i/2对称的
            if i/2>int(i/2):
                k = int(i/2) + 1
            elif i/2==int(i/2):
                k = int(i/2)

            for j in range(1, k+1):
                # li[j]表示长度为j时的最优解
                temp = li[j]*li[i-j]
                if temp>max:
                    max = temp
            li.append(max)
        # print(li)
        return li[-1]


test = Solution()
print(test.cutRope(8))
print(test.cutRope(100))

'''
方法二：用贪婪算法进行解题
'''
class Solution:
    def cutRope(self, length):
        if length<2:
            return 0
        if length==2:
            return 1
        if length==3:
            return 2

        # 整除3余数为1时，当做特殊情况处理：因为最后3+1=4，这个4不能拆为3+1，二是拆为2+2，这样最大乘积为4而不是3
        # %是取余数，//是取整数部分；
        if length%3==1:
            if length//3>1:
                return 3**(length//3-1)*4
            elif length//3==1:
                return 4
        elif length%3==2:
            return 3**(length//3)*2
        elif length%3==0:
            return 3**(length//3)


test = Solution()
print(test.cutRope(8))
print(test.cutRope(100))

