'''
题目：请完成一个函数，输入一个二叉树，该函数输出它的镜像

思路：
采用递归的方式，每次对调根节点下的左右子节点

'''

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def mirrorOfBinaryTree(root):
    if root is None:
        return None

    # 先处理根节点
    root.left, root.right = root.right, root.left
    # 再处理左子树
    mirrorOfBinaryTree(root.left)
    # 最后处理右子树
    mirrorOfBinaryTree(root.right)

if __name__=='__main__':
    print()
    ''' 本地应该怎么进行测试，应为不能有输出 '''