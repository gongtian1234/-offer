'''
题目：输入一颗二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点往下一直到叶节点所经过的结点形成一条路径
（注意：第一，路径指的是从根节点到叶子节点的一条完整的路径）

思路：
根据广度优先的方法，依次去寻找路径和为输入整数的路径(看代码吧，不太明白)

'''
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def findPath(root, expectedSum):
    if root is None:
        return []
    if root.left is None and root.right is None and root.val==expectedSum:
        return [[root.val]]
    else:
        rst = []
        left = findPath(root.left, expectedSum-root.val)
        right = findPath(root.right, expectedSum-root.val)
        print('当前的root值为',root.val)
        print('left is ',left)
        print('right is ',right)
        # print('left+right is ',left+right)
        for item in left+right:    # 这一步是为了把当前root的值添加到每一个符合的列表中去
            rst.append([root.val]+item)
        return rst

if __name__=='__main__':
    '''
                                   10
                            5                6
                        4       7         1      6
    '''
    t1,t2,t3,t4,t5,t6,t7 = TreeNode(10),TreeNode(5),TreeNode(6),TreeNode(4),TreeNode(7),TreeNode(1),TreeNode(6)
    t1.left = t2
    t2.left = t4
    t2.right = t5
    t1.right = t3
    t3.left = t6
    t3.right = t7
    print(findPath(t1, 22))

