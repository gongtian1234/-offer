'''
面试题13：机器人的运动范围。地上有一个m行n列的格子。一个机器人从坐标(0,0)的位置开始移动，每次可以向左右上下移动一格，但不能进入
          行坐标和列坐标位数之和大于k的格子。如k=18时，机器人可以进入(35,37), 但不能进入(35,38)。问该机器人能到达多少个格子？

思路：
对比：矩阵中的路径中使用了for循环先匹配首字母，匹配成功后在其上下左右匹配下一个字母，匹配成功后，再匹配下一个字母；否则表明该路径不
      通，重新用for匹配首字母；
      机器人的运动范围中没有使用for，因为这个题不用先匹配首字母再匹配下一个，相当于首字母给出，需要不断以上下左右的方式寻找满足条件
      的下一个，直至到路的尽头为止，具体还得结合demo理解。

问题：movingCountCore()的递归没有绕明白，check通过进入一个点后，开始上下左右测试，先上递归，上面如果通过check，在这一个点再上下左右
      递归，直到到达尽头为止【有点不撞南墙不回头的意思，在一个满足的点上，没有找到尽头是不会结束递归的】
'''

class Solution:
    def movingCount(self, threshold, rows, cols):
        if threshold<0 or rows<=0 or cols<=0:
            return 0
        visited = [False]*(rows*cols)
        count = self.movingCountCore(rows, cols, threshold, 0, 0, visited)
        return count

    def movingCountCore(self, rows, cols, threshold, row, col, visited):
        count = 0
        if self.check(rows, cols, threshold, row, col, visited):
            visited[row*cols+col] = True
            count = 1 + \
                    self.movingCountCore(rows, cols, threshold, row-1, col, visited) + \
                    self.movingCountCore(rows, cols, threshold, row+1, col, visited) + \
                    self.movingCountCore(rows, cols, threshold, row, col-1, visited) + \
                    self.movingCountCore(rows, cols, threshold, row, col+1, visited)
        return count

    def check(self, rows, cols, threshold, row, col, visited):
        if row>=0 and row<rows and col>=0 and col<cols and (self.getDigitSum(row)+self.getDigitSum(col)<=threshold) and not visited[row*cols+col]:
            return True
        return False

    def getDigitSum(self,num):
        sum = 0
        while num>0:
            sum += (num%10)
            num = num//10
        return sum

test1 = Solution()
print(test1.movingCount(5, 10, 10))
print(test1.movingCount(10,1,100))


# 这种解法不考虑机器人，仅考虑在限定的格子内能到达多少个点，但是以下这种方法还是有点暴力，可以考虑一下更优化的方法
##【注意：好像跑题了，题目问的是能到达多少个格子，不是能到达多少个点；原题中的上下左右走法其实就限定了是格子】##
class Solution2:
    def movingCount(self,threshold, rows, cols):
        if threshold<0 or rows<=0 or cols<=0:
            return 0

        count_lst = []
        for row in range(rows):
            for col in range(cols):
                str_row, str_col = str(row), str(col)
                n_r, n_c = len(str_row), len(str_col)
                n_sum = 0
                for i in range(n_r):
                    n_sum += int(str_row[i])
                for j in range(n_c):
                    n_sum += int(str_col[j]) 
                if threshold>=n_sum:
                    count_lst.append(1)
                else:
                    continue
        return len(count_lst)

test2 = Solution2()
# print(test.movingCount(500,500,75))    # 250000  1.1s
print(test2.movingCount(5, 10, 10))      
print(test2.movingCount(10,1,100))      
