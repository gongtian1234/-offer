'''
题目：求1+2+……+n，要求不能用乘除法、for、while、if、else等关键字及条件判断语句

思路：
发散性思维，在实际中不太可能出现。
'''

def sumSolution(n):
    return n and (n+sumSolution(n-1))

if __name__ == '__main__':
    print(sumSolution(5))