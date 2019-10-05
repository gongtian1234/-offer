'''
题目：用两个栈实现一个队列。队列的声明如下，实现它的两个函数appendTail和deleteHead, 分别完成在队列尾部插入节点和在队列头部删除节点。

思路：
首先清除一点：列表类似于栈，所以可以用列表创建两个栈stack；
其次，在添加元素时都添加到stack1；在输出时，判断stack2是否为空，为空则把stack1的元素pop进stack2，若stack2不为空，则直接pop stack2的元素；
这样就通过两个栈构造出了队列。
'''
class Solution:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def appendTail(self, element):
		self.stack1.append(element)

	def deleteHead(self):
		if len(self.stack1)==0 and len(self.stack2)==0:
			return
		if len(self.stack1)>0 and len(self.stack2)==0:
			while len(self.stack1)>0:
				self.stack2.append(self.stack1.pop())
		return self.stack2.pop()


test = Solution()
# 测试一：往空的队列里添加和删除元素
test.appendTail(5)
print(test.deleteHead())

# 测试二：往非空的队列里添加和删除元素
test.appendTail(6)
test.appendTail(7)
test.appendTail(8)
test.appendTail(9)
test.appendTail(10)
test.appendTail(11)
test.appendTail(12)
print(test.deleteHead())    # 此时元素6已经被pop出来了
print()

# 测试三：连续删除元素，直至队列为空
a = test.deleteHead()
while a:
	print(a)
	a = test.deleteHead()


'''
补充：python的列表就可以看做是一个栈，后进先出（LIFO）
'''