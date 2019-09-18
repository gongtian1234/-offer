'''
题目：输入一个列表的头节点，从尾到头反过来打印出每个节点的值

思路：链表从头到尾输出非常简单，但是从尾到头却不容易；先从头到尾遍历一遍，典型的先进后出，将元素存于栈中

功能测试：输入的链表有多个节点；输入的列表只有一个节点
特殊输入测试：输入的链表头节点指针为空

补充：环形链表：面试题62“圆圈中最后剩下的数字”
	  双向链表：面试题36“二叉树搜索与双向链表”
	  复杂链表：面试题35“复杂链表取得复制”
'''

class Node:
	'''创建单个节点'''
	def __init__(self, val=None):
		self.val = val
		self.next = None


class Solution:
	def printListFromTail2Head(self, listnode):
		if listnode.val==None:    # 首节点为空的情况（即传入的链表是一个空链表）
			return '该链表为空链表'
		elif listnode.next==None and listnode.val is not None:    # 传入的链表只有一个节点
			return listnode.val
		else:
			lst = []
			cur = listnode
			while cur.next is not None:    # 这么写会漏掉最后一个节点的值, 所以要在最后把漏掉的情况补上
				lst.insert(0,cur.val)
				if cur.next is not None:
					cur = cur.next
			if cur.next is None:
				lst.insert(0, cur.val)
			return lst



# 先创建一个链表
node1 = Node(12)
node2 = Node(16)
node3 = Node(19)
node4 = Node()
node5 = Node(9)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node6 = Node()
node7 = Node(1)

print(node2.next.val)    # 19(说明已将其组成链表)

# 开始测试
ss = Solution()

print('首节点为空:',ss.printListFromTail2Head(node6))    # 首节点为空
print('只有一个节点:',ss.printListFromTail2Head(node7))    # 只有一个节点
print('一般情况:',ss.printListFromTail2Head(node1))    # 19

