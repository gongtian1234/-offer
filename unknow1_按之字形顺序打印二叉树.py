'''
题目：请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三层按照从左到右的顺序打印，
依次类推

思路：
①按照广度优先的思路执行不通，因为很难区分清楚打印到第几层，从而没办法及时调整方向（从左到右还是从右到左）
②找两个栈，将奇数层的结点从右到左append进去，将偶数层的结点从左到右append进去，最后再从尾部pop出来
'''
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def Print(root):
    if root is None:
        return []
    stack1 = [root]   # 奇数层的结点存入stack1
    stack2 = []       # 偶数层的结点存入stack2
    rst = []

    while stack1!=[] or stack2!=[]:
        if stack1!=[]:
            tmpRst = []
            while stack1:
                tmpNode = stack1.pop()
                tmpRst.append(tmpNode.val)
                if tmpNode.left is not None:
                    stack2.append(tmpNode.left)
                if tmpNode.right is not None:
                    stack2.append(tmpNode.right)
            rst.append(tmpRst)

        if stack2!=[]:
            tmpRst = []
            while stack2:
                tmpNode = stack2.pop()
                tmpRst.append(tmpNode.val)
                if tmpNode.right is not None:
                    stack1.append(tmpNode.right)
                if tmpNode.left is not None:
                    stack1.append(tmpNode.left)
            rst.append(tmpRst)
    return rst


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
