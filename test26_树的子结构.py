'''
题目：输入两颗二叉树A和B，判断B是不是A的子结构（注意：约定空树不是任意树的子结构）

思路：
主要是分为三种情况处理：第一种，二者的根节点就相同；第二种，B是A的左子树的一部分；第三种，B是A的右子树的一部分；针对每一种情况再判断B是否是A
的子结构（如何判断：先判断根节点是否相等，如果相等，再分别去判断左、右两边是否相等，整体相等才能返回True，否则只能返回false）

'''

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None



def hasSubTree(treeA, treeB):
    if treeA is None or treeB is None:
        return False

    def hasEqual(treeA, treeB):
        if treeB is None:
            return True
        if treeA is None:
            return False
        if treeA.val == treeB.val:
            # 判断左子树是否相等
            if treeB.left is None:
                leftEqual = True
            else:
                leftEqual = hasEqual(treeA.left, treeB.left)
            # 判断右子树是否相等
            if treeB.right is None:
                rightEqual = True
            else:
                rightEqual = hasEqual(treeA.right, treeB.right)
            return leftEqual and rightEqual
        return False

    # 两棵树的根节点相等，只有当根结点的值相等时才能进入hasEqual函数进行判断
    if treeA.val == treeB.val:
        ret = hasEqual(treeA, treeB)
        if ret:
            return True

    # 当两棵树的根节点不相等时，先递归判断左子树与B的关系
    ret = hasSubTree(treeA.left, treeB)
    if ret:
        return True

    # 再递归判断右子树与B的关系
    ret = hasSubTree(treeA.right, treeB)
    return ret

if __name__=='__main__':
    t1, t2, t3, t4, t5, t6, t7, t8 = TreeNode(1),TreeNode(2),TreeNode(3),TreeNode(4),TreeNode(5),TreeNode(6),TreeNode(7),TreeNode(8)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    t6.right = t8

    u1, u2 = TreeNode(2), TreeNode(4)
    u1.left = u2

    print(hasSubTree(t1, u1))