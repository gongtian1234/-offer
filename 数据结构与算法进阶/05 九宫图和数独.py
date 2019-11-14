'''
题目：九宫图(与数独规则不一样)。每一行每一列以及对角线的元素加起来和相等（注：九宫图的行数与列数必然为奇数）

思路：
首先要了解一个算法，每次把1放在最后一行的中间位置，然后另其右下方的数为2，超出边界，则对应找对角线上的位置，再在右下角
填3，依次类推，如果发现下一个位置是1，则把下一个数填在这一对角线结束的上方的那个格子里，再与之前的循环操作类似，直至把最后一个数填进格
为止【注：知道了这个解题方法后，关键是怎么用程序写出来】
注意：
首先，要搞清楚游戏规则；
其次，（技巧）要处理好越界问题，当下一个元素的位置超出边界时，通过取余让其重新回到边界内；
最后，写出程序的时间复杂度为O(n)
'''

def magic_square(num):
    magic = [[0 for i in range(num)] for j in range(num)]
    row = num - 1
    col = num // 2  # //是整除，%是取余
    magic[row][col] = 1  # 最后一行中间位置的元素设为1
    for i in range(2, num**2+1):  # 九宫格中数的取值范围
        row = (row+1)%num         # 【关键点：取余这个操作】
        col = (col+1)%num
        if magic[row][col]==0:
            magic[row][col] = i
        else:
            row = (row-2+num)%num   # 加上num是为了防止出现负数
            col = (col-1+num)%num
            magic[row][col] = i
    for tmp in magic:
        print(tmp)

magic_square(9)

'''
题目：数独。在9*9的格子里，每一行每一列以及每一个切分好的3*3的格子里，1~9都仅出现一次。给一个填好的数独，验证其是否正确。
思路：用for循环，然后再判断行列以及3*3的单元里面元素是否为1~9，用set(这个题我已经绕懵圈了)
'''

def yanzhengshudo(magic):
    for i in range(9):
        # 验证行: 每行的数为1~9
        if len(set(magic[i]))<9 or max(magic[i])>9 or min(magic[i])<1:
            return False

        # 验证列
        col_lst = []
        for rowi in range(9):
            col_lst.append(magic[rowi][i])
        if len(set(col_lst))<9 or max(col_lst)>9 or min(col_lst)<1:
            return False

        # 验证3*3的单元：共有9个3*3的单元
        if i not in [0,3,6]:
            continue 
        for ii in [0,3,6]:
            tmps = []
            for j in range(i, i+3):
                tmps.append(magic[ii][j])   # 这里的i标记的是行
                tmps.append(magic[ii+1][j])
                tmps.append(magic[ii+2][j])
            if len(set(tmps))<9 or max(tmps)>9 or min(tmps)<1:
                return False
    return True

magics = [[5,3,4,6,7,8,9,1,2],
          [6,7,2,1,9,5,3,4,8],
          [1,9,8,3,4,2,5,6,7],
          [8,5,9,7,6,1,4,2,3],
          [4,2,6,8,5,3,7,9,1],
          [7,1,3,9,2,4,8,5,6],
          [9,6,1,5,3,7,2,8,4],
          [2,8,7,4,1,9,6,3,5],
          [3,4,5,2,8,6,1,7,9]]
print(yanzhengshudo(magics))