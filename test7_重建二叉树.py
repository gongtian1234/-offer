'''
输入前序遍历和中序遍历重建二叉树：
规律：前序遍历的第一个数字总是根节点；中序遍历中根节点的左端为左子树，右端为右子树
'''

class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.leftChild = None
        self.rightChild = None


class Solution:
    def reBuildBinaryTree(self, tpre, tin):     # Preorder traversal; In-order traversal
        len_li = len(tpre)
        if len_li==0:
            # 返回一颗空树
            return TreeNode()
        elif len_li==1:
            return TreeNode(tpre[0])
        else:
            try:
                root_loc = tin.index(tpre[0])    # 寻找根节点在中序遍历中的位置
                root = TreeNode(tpre[0])
                # 递归就是直接或间接调用函数本身
                root.leftChild = self.reBuildBinaryTree(tpre=tpre[1:1+len(tin[:root_loc])], tin=tin[:root_loc])    # 这个过程就是递归，自己调用自己
                root.rightChild = self.reBuildBinaryTree(tpre=tpre[1+len(tin[:root_loc]):], tin=tin[root_loc+1:])
                return root
            except:
                print('【注意】前序遍历和中序遍历不匹配，以下打印的树是错误的')

# 1、创建一颗正常的树
tpre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]
test = Solution()
tree = test.reBuildBinaryTree(tpre, tin)

# 2、创建一颗空树
# tpre = []
# tin = []
# test = Solution()
# tree = test.reBuildBinaryTree(tpre, tin)
# print(tree)              # <__main__.TreeNode object at 0x000000E6C3815668>
# print(tree.leftChild)    # None
# print(tree.leftChild.val)# 报错
# if tree.leftChild is None:
#     print(1)

# 3、前序遍历和中序遍历不匹配
# tpre = [1,2,4,7,3,6,5,8]
# tin = [4,7,2,1,5,3,6,8]
# test = Solution()
# tree = test.reBuildBinaryTree(tpre, tin)

def printTree(node1):
    '''以先序遍历的方式打印出二叉树'''
    if node1 is None:
        return
    print(node1.val, end=' ')
    printTree(node1.leftChild)
    printTree(node1.rightChild)
printTree(node1=tree)    # 1 2 4 None 7 None 3 5 6 8 None(这种便利方式有None，可以考虑在打印出来之前判断一下是否为None【空值是创建二叉树时，每个叶节点后跟两个左右子孩的空值】)
