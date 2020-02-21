# coding=utf-8
'''
题目：给定一颗二叉树和其中的一个节点，找出中序遍历的下一个节点。其中已知该节点的左右子节点和该节点的父节点。

思路：
先在纸上画一颗满二叉树
1> 情况1：如果该节点有右子树，则下一个节点就是右子树的最左节点(用while寻找右子树的最左节点)；
2> 情况2：如果该节点没有右子树，且其是左子树下的，则下一个节点就是其父节点；或者其是右子树下的，则下一个节点就要一直往上溯源，否则返回None
'''
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None    # 指向该节点的父节点


class Solution:
    def GetNext(self, pNode):
        # writing code here
        if not pNode:    # if True (防止传入空节点)
            return pNode

        if pNode.right:  # 右子树不为空
            tmpNode = pNode.right
            while tmpNode.left:
                tmpNode = tmpNode.left
            return tmpNode
        else:
            tmpNode = pNode
            while tmpNode.next:# 非根节点
                if tmpNode==tmpNode.next.left:
                    return tmpNode.next
                tmpNode = tmpNode.next
            return None


'''
参考文章：
1. https://www.cnblogs.com/yuling-chao/p/7323762.html《二叉树的下一个节点》
2. https://blog.csdn.net/chocolate_chuqi/article/details/81075423《剑指offer 面试题8 （二叉树的下一个节点） python》
'''