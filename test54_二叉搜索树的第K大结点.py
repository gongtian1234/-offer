'''
题目：给定一颗二叉搜索树，请找出其中第k个最小结点值（书上的意思还是找出第k个最小值）。例如(5,3,7,2,4,6,8)中，按结点数值大小顺序第三小结点的值
为4（补充：二叉搜索树：左子树都小于父节点，右子树都大于父节点）
                        5
            3                          7
         2     4                    6      8

思路：
等价于中序遍历找第k个值
'''

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def KthNode(root,k):
    if root is None or k<1:
        return None

    nodeList = []
    def preOrder(root):
        if root is None:
            return None

        preOrder(root.left)
        nodeList.append(root)
        preOrder(root.right)

    preOrder(root)
    if len(nodeList)<k:
        return None
    return nodeList[k-1]
