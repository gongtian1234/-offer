'''
题目：旋转数组。给定一个n*n的数组，将其顺时针旋转90度。

思路：
1、创建一个n*n的数组，将对应的元素存入新数组中，但是有O(n^2)的空间复杂度；
2、先转置再左右翻转，优点：没有占用新空间；【注意：根据这种方法可以求出旋转90度、180度（先上下翻转再左右翻转）、
   270度（就是逆时针旋转90度）等】
   参考网址：https://blog.csdn.net/shahuzi/article/details/97825167
'''

#### 方法一 ####
def rotate(matrix):
    n = len(matrix)
    new_matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            new_matrix[j][n-1-i] = matrix[i][j]
    for tmp in new_matrix:
        print(tmp)
rotate([[1,2,3],
        [4,5,6],
        [7,8,9]])

#### 方法二 ####
def rotate2(matrix):
    n = len(matrix)
    # 先将矩阵转置
    for i in range(n):
        for j in range(i, n):  # 逐个元素进行转置
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # 再进行水平翻转处理
    for i in range(n):
        matrix[i].reverse()
    for tmp in matrix:
        print(tmp)
rotate2([[1,2,3],
         [4,5,6],
         [7,8,9]])
import os
os.system("pause")
