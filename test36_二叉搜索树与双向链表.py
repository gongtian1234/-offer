'''
题目：输入一颗二叉搜索树，将该二叉搜索树转换为一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向

思路：
参考网址：https://blog.csdn.net/u010005281/article/details/79657259作者讲的很详细。
借用两个辅助变量分别标记双向链表的头节点和尾节点，按照中序遍历的思路，用递归进行解题
'''

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.listHead = None
        self.listTail = None

    def convert(self, root):
        if root is None:
            return 

        self.convert(root.left)
        if self.listHead is None:
            self.listHead = root
            self.listTail = root
        else:
            self.listTail.right = root
            root.left = self.listTail
            self.listTail = root
        self.convert(root.right)
        return self.listHead

if __name__=='__main__':
    '''
二叉搜索树的结构为：               8
                            6              10
                          5    7         9     11
    '''
    t1,t2,t3,t4,t5,t6,t7 = TreeNode(8),TreeNode(6),TreeNode(10),TreeNode(5),TreeNode(7),TreeNode(9),TreeNode(11)
    t1.left = t2
    t2.left = t4
    t2.right = t5
    t1.right = t3
    t3.left = t6
    t3.right = t7
    s = Solution()
    print(s.convert(t1))
