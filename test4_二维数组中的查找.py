# 二维数组中的查找：
# 对于在一个每一行从左到右依次递增，每一列从上到下依次递增的二维数组查找一个元素，
# 可以选择从数组左上角开始查找array[i][j]，如果目标元素大于array[i][j]，i+=1，
# 如果元素小于array[i][j]，j-=1，依次循环直至找到这个数。
# 也可以从右下角开始查找

'''
可能发生的特殊情况：
1、要查找的字符不是int类型，不能比较大小；
2、数组中有字符串时，不能比较大小；
3、【这里只研究纯数字的情况】
'''

import numpy as np


lst = []
def find(matrix, num):
    cols = len(matrix[0])
    rows = len(matrix)
    if type(num)==str:
        print('要查找的值为数值型')
        return False
    elif cols!=0 and rows!=0:
        row = 0
        col = cols - 1
        while row<rows and col>=0:
            if arr[row][col]==num:
                lst.append((row, col))
                print((row, col))
                return True
            elif arr[row][col]>num:
                col -= 1
            elif arr[row][col]<num:
                row += 1
    else:
        print('数组为空')
        return False



if __name__=='__main__':
    arr = np.array([[1,2,3],[4,5.0,6],[7,8,9],[10,11,12]])
    arr = [[1,2,3],[4,5.0,6],[7,8,9],[10,11,12]]
    # arr = np.array([[],[],[]])
    num = 8
    print(find(arr, 5.0))
    if len(lst)==0:
        print('在二维数组中未找到该元素')
    else:
        print(lst)


'''
规律总结：
首先选取数组中右上角的数字。
①如果该数字等于要查找的数字，则查找过程结束；
②如果该数字大于要查找的数字，则剔除该数字所在的列；
③如果该数字小于要查找的数字，则剔除该数字所在的行。
即如果要查找的数字不在右上角，则剔除其所在的列或行。
'''