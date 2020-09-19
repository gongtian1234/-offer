# leetcode124: 二叉树中的最大路径和
# 起始点和结束点可以是任一节点（只要不违背树的三种遍历方式就可以）

class Solution:
    def __init__(self):
        self.max_sum = -float('inf')
        
    def maxPathSum(self, root):
        if root is None:
            return 0
        left = self.maxPathSum(root.left)
        right = self.maxPathSum(root.right)
        self.max_sum = max(self.max_sum, root.val + left +right)
        return max(0, root.val+max(left, right))
        
