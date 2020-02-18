'''
题目：从上往下打印出每个二叉树的节点，同一层的节点按照从左到右的顺序打印

思路：
将树的每一个左右节点都按照左右的顺序放入队列中，然后再按照先进先出的顺序打印出该节点的值，再将它的左右子节点放入队列中
'''

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


def printFromTopToBottom(root):
    if root is None:
        return 
    queue = [root]
    while queue:
        curNode = queue.pop(0)
        print(curNode.val,end=' ')
        if curNode.left is not None:
            queue.append(curNode.left)
        if curNode.right is not None:
            queue.append(curNode.right)

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

    printFromTopToBottom(t1)