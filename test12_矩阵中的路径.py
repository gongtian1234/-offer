'''
题目：矩阵中的路径。设计一个函数用来判断一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵的任意一格开始，
      每一步都可以在矩阵中向左、右、上、下移动一格。如果一条路径中包含了矩阵的某一格，那么该路径不能进入该格子。【提示：
      用的是回溯法，回溯法适合有多个步骤且每个步骤都有很多选项的问题，通过遍历式的尝试找到最优的可行方案】

思路：采用回溯法进行解题，每到一个格子都有上下左右四步走法，用循环用第一行第一列的元素开始往下寻找，若该位置的元素等于
      要寻找的元素时进入递归以查看其上下左右是否能匹配下一个元素，否则返回上一级；其实就是找到首字母后才会进入递归，进
      一步判断其上下左右是否有符合的，否则重新返回到for循环，寻找下一个匹配成功的首字母。【稍微有点绕】
'''

class Solution:
    def hasPath(self, matrix, rows, cols, string):
        if len(matrix)==0 or rows<1 or cols<1 or string is None:
            return False

        visited = [0] * len(matrix)
        str_i = 0
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, string, row, col, visited, str_i):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, string, row, col, visited, str_i):
        if len(string)==str_i:
            return True

        hasPath = False
        
        if row>=0 and row<rows and col>=0 and col<cols and matrix[row*cols+col]==string[str_i] and not visited[row*cols+col]:
            str_i += 1
            visited[row*cols+col] = True

            hasPath = self.hasPathCore(matrix, rows, cols, string, row-1, col, visited, str_i) or \
                      self.hasPathCore(matrix, rows, cols, string, row+1, col, visited, str_i) or \
                      self.hasPathCore(matrix, rows, cols, string, row, col-1, visited, str_i) or \
                      self.hasPathCore(matrix, rows, cols, string, row, col+1, visited, str_i)
            if not hasPath:
                str_i -= 1
                visited[row*cols+col] = False

        return hasPath


test = Solution()
print(test.hasPath(matrix=['a','i','b','c', 'd','l','v','y', 'e','f','g','h'], rows=3, cols=4, string='ilvy')) # True
print(test.hasPath(matrix=[], rows=3, cols=4, string='ilvy'))                                                  # False
print(test.hasPath(matrix=['a','i','b','c', 'd','l','v','y', 'e','f','g','h'], rows=3, cols=4, string=''))     # True
print(test.hasPath("ABCESFCSADEE", 3, 4, "ABCCED"))                                                            # True