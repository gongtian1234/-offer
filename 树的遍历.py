'''
树的知识储备
首先树通常分为两类：广义优先和深度优先

广义优先：横着读取树上的数据（看面试题32，考察的就是广度优先遍历二叉树）
深度优先：读取数据的方式有分为三种：先序遍历（根左右）、中序遍历（左根右）和后续遍历（左右根）【指的是根的位置】

其中，深度优先是最常使用的方法，以下会以递归和循环的方式编写深度优先的三种数据存储方式【循环的方式没整明白】
'''

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


''' 方法一：以递归的方式编写深度优先 '''
def preOrderRecusive(root):
    if root is None:
        return
    print(root.val, end=' ')
    preOrderRecusive(root.left)
    preOrderRecusive(root.right)

def midOrderRecusive(root):
    if root is None:
        return 
    midOrderRecusive(root.left)
    print(root.val, end=' ')
    midOrderRecusive(root.right)

def latOrderRecusive(root):
    if root is None:
        return
    latOrderRecusive(root.left)
    latOrderRecusive(root.right)
    print(root.val, end=' ')

''' 方法二：以循环的方式编写深度优先 '''
def preOrder(root):
    if root is None:
        return

    stack = []
    tmpNode = root
    while tmpNode or stack:
        while tmpNode:
            print(tmpNode.val, end=' ')
            stack.append(tmpNode)
            tmpNode = tmpNode.left

        node = stack.pop()
        tmpNode = node.right

def midOrder(root):
    if root is None:
        return
    
    stack = []
    tmpNode = root
    while tmpNode or stack:
        while tmpNode:
            stack.append(tmpNode)
            tmpNode = tmpNode.left
        node = stack.pop()
        print(node.val, end=' ')
        tmpNode = node.right

def latOrder(root):
    if root is None:
        return 

    stack = []
    tmpNode = root
    while tmpNode or stack:
        while tmpNode:
            stack.append(tmpNode)
            tmpNode = tmpNode.left
        node =stack[-1]
        tmpNode = node.right
        if node.right is None:
            node = stack.pop()
            print(node.val, end=' ')
            while stack and node == stack[-1].right:
                node = stack.pop()
                print(node.val, end=' ')

if __name__=='__main__':
    '''
    树的结构为：
                                   1
                            2             3
                          4    5      6      7
                                        8
    '''
    t1, t2, t3, t4, t5, t6, t7, t8 = TreeNode(1),TreeNode(2),TreeNode(3),TreeNode(4),TreeNode(5),TreeNode(6),TreeNode(7),TreeNode(8)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    t6.right = t8

    print('方法1（递归的方式）：')
    print('先序遍历结果为：',end='')
    preOrderRecusive(t1)
    print()
    print('中序遍历结果为：',end='')
    midOrderRecusive(t1)
    print()
    print('后序遍历结果为：',end='')
    latOrderRecusive(t1)
    print()
    
    print('方法2（循环的方式）：')
    print('先序遍历结果为：',end='')
    preOrder(t1)
    print()
    print('中序遍历结果为：',end='')
    midOrder(t1)
    print()
    print('后序遍历结果为：',end='')
    latOrder(t1)
    print()

