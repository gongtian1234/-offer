'''
题目一：二叉树的深度。输入一颗二叉树的根节点，求该树的深度，从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的
长度为树的深度。

思路：
参考网址：https://blog.csdn.net/dailu11/article/details/80609416?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
自己做不会，但是一看别人的（哦，好像是那么回事；对递归理解还是不到位）

题目二：平衡二叉树。输入一颗二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树深度相差不超过1，那么它就是一颗平衡二叉树

思路：
根据二叉树深度的思路，判断其左右子树的最大深度并进行比较，如果大于1，直接返回False，否则再进一步判断其子树是否满足, 这种方法每个节点只需要遍历一
次即可
'''

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def maxDepth(self, root):

        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

class Solution2:
    def isBalanced(self, root):
        ''' 判断是不是一颗平衡二叉树 '''
        if root is None:
            return True
        if 1<abs(self.maxDepth(root.left)-self.maxDepth(root.right)):
            return False
        else:
            left = self.isBalanced(root.left)
            right = self.isBalanced(root.right)
            return left and right


    def maxDepth(self, root):
        ''' 判断子树的最大深度 '''
        if root is None:
            return 0
        else:
            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)
            return 1+max(leftDepth, rightDepth)


if __name__ == '__main__':
    '''
            3
      5          6
    8   9      1    2
                       7
    '''
    t1,t2,t3,t4,t5,t6,t7,t8 = TreeNode(3),TreeNode(5),TreeNode(6),TreeNode(8),TreeNode(9),TreeNode(1),TreeNode(2),TreeNode(7)
    t1.left, t1.right = t2, t3
    t2.left, t2.right = t4, t5
    t3.left, t3.right = t6, t7
    t7.right = t8
    s1 = Solution1()
    print(s1.maxDepth(t1))

    s2 = Solution2()
    t9 = TreeNode(10)
    t8.left = t9
    print(s2.isBalanced(t1))
    print(s2.maxDepth(t1.right))