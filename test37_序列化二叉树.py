'''
题目：请实现两个函数，分别用来序列化和反序列化二叉树

思路：
序列化的过程就是对树进行前序遍历，但是要注意找一个记号（如'#'）标记叶子结点；
反序列化的过程将序列转换为树结构。先将字符串且分为列表格式，再根据所做的叶子结点的标记采用递归的方法，找出左右子节点从而还原为一棵树
'''

class Solution:
    def serialize(self, root):
        if root is None:
            return
        rstList = []
        def preOrder(root):
            # 前序遍历
            if root is None:
                rstList.append('#')
                return 

            rstList.append(str(root.val))
            preOrder(root.left)
            preOrder(root.right)
        
        preOrder(root)
        return ' '.join(rstList)     # 将列表转换为一个字符串

    def deserialize(self,s):
        if not s:
            return 

        rstList = s.split(' ')

        def toTree():
            rootVal = rstList.pop(0)
            if rootVal=='#':
                return None
            node = TreeNode(int(rootVal))
            leftNode = toTree()
            rightNode = toTree()
            node.left = leftNode
            node.right = rightNode
            return node

        root = toTree()
        return root

