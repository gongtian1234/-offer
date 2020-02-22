'''
题目：从上到下打印二叉树，同一层结点从左到右输出，每一层输出一行

思路：
与上一个按之字形打印二叉树的题目高度相似，只是把上一个题用的栈换为队列
'''

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def Print(root):
    if root is None:
        return []
    queue1 = [root]
    queue2 = []
    values = []
    while queue1!=[] or queue2!=[]:
        if queue1!=[]:
            tmpValue = []
            while queue1!=[]:
                tmpNode = queue1.pop(0)
                tmpValue.append(tmpNode.val)
                if tmpNode.left is not None:
                    queue2.append(tmpNode.left)
                if tmpNode.right is not None:
                    queue2.append(tmpNode.right)
            values.append(tmpValue)

        if queue2!=[]:
            tmpValue = []
            while queue2!=[]:
                tmpNode = queue2.pop(0)
                tmpValue.append(tmpNode.val)
                if tmpNode.left is not None:
                    queue1.append(tmpNode.left)
                if tmpNode.right is not None:
                    queue1.append(tmpNode.right)
            values.append(tmpValue)
    return values

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
    print(Print(t1))

