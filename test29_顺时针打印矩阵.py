'''
题目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出矩阵的每一个数字。如，矩阵
1  2  3  4
5  6  7  8
9  10 11 12 
13 14 15 16
打印出的顺序为1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

思路：
用while循环顺时针打印，循环条件row<rows/2 and column<columns/2（如，5*5或6*6的矩阵，结束的左上角点的坐标为(2,2)）。分四次打印，
先从左到右，再从上到下，再从右到左，最后从下到上
'''

def printMatrixClockwisely(numbers):
    if numbers is None or numbers==[]:
        return
    rows = len(numbers)
    columns = len(numbers[0])
    row, column = 0, 0
    i = 0    # 用来记录目前是第几层（从外往里）
    printNum = []
    while row<rows/2 and column<columns/2:
        tmpX, tmpY = row, column
        # 先从左到右打印
        for startY in range(0+i, columns-i):
            printNum.append(numbers[tmpX][startY])
        tmpY = columns-i-1

        # 从上到下打印
        if 0+i+1<rows:
            for startX in range(0+i+1,rows-i):
                printNum.append(numbers[startX][tmpY])
        tmpX = rows-i-1

        # 从右往左打印
        if columns-i-1-1>0+i-11:
            for startY in range(columns-i-1-1, 0+i-1,-1):    # 第一个-1是因为索引从0开始的，第二个-1是避免重复打印右下角的值
                printNum.append(numbers[tmpX][startY])
        tmpY = 0+i

        # 从下往上打印
        if rows-i-1-1>0+i:
            for startX in range(rows-i-1-1, 0+i, -1):
                printNum.append(numbers[startX][tmpY])
                
        row += 1
        column += 1
        i += 1
    return printNum

if __name__ == '__main__':
    print(printMatrixClockwisely([[7,8,9],[4,5,6],[1,2,3]]))
    print(printMatrixClockwisely([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))

