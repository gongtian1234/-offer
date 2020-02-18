'''
题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则返回True，否则输出False。假设输入数组的任意两个数字都互不相同
（名词解释：二叉搜索树————左子树的值必然小于根节点，右子树的值必然大于根节点的值；或者是一颗空树）

思路：
二叉搜索树的后序遍历，如5 7 6 9 11 10 8，8是根节点，根据二叉树的性质判断出5 7 6 是左子树的（都小于8），9 11 10是右子树的（都大于8），再递归
进行判断，如果应该是右子树的部分出现小于根结点的（如小于8），则输出False
'''

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


def verifySquenceOfBST(sequence):
    if sequence==[]:
        return True   # 因为空树也是搜索二叉树

    rootNum = sequence.pop()
    index = None      # 用来标记左右子树的分界线，指向的是右子树的节点位置
    for i in range(len(sequence)):
        if index is None and sequence[i]>rootNum:
            index = i
        if index is not None and sequence[i]<rootNum:
            return False
    leftRst = verifySquenceOfBST(sequence[:index])
    rightRst = verifySquenceOfBST(sequence[index:])

    return leftRst and rightRst

if __name__=='__main__':
    '''
二叉搜索树的结构为：               8
                            6              10
                          5    7         9     11
    '''
    t1, t2, t3, t4, t5, t6, t7 = TreeNode(8),TreeNode(6),TreeNode(10),TreeNode(5),TreeNode(7),TreeNode(9),TreeNode(11)
    t1.left = t2
    t2.left = t4
    t2.right = t5
    t1.right = t3
    t3.left = t6
    t3.right = t7
    print(verifySquenceOfBST([5,7,6,9,11,10,8]))

