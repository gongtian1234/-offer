'''
题目：请实现一个函数，用来判断一颗二叉树是不是对称的。如果一颗二叉树和它的镜像一样，那么它就是对称的，否则不是

思路：
采用递归的方法，判断左子树的左边是否与右子树的右边相等，左子树的右边是否与右子树的左边相等

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetrical(root):
    if root is None:
        return True

    def isMirror(left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        if left.val != right.val:
            return False
        leftRst = isMirror(left.left, right.right)
        rightRst = isMirror(left.right, right.left)

        return leftRst and rightRst

    return isMirror(root.left, root.right)


if __name__=='__main__':
    '''
              8
        6          6
     5     7     7   5 
    '''
    t1, t2,t3,t4,t5,t6,t7 = TreeNode(8),TreeNode(6),TreeNode(6),TreeNode(5),TreeNode(7),TreeNode(7),TreeNode(5)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    print(isSymmetrical(t1))