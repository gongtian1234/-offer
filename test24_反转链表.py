'''
题目：定义一个函数，输入链表的头节点，反转该链表并输出反转后链表的头节点。（就是要求把一个单向链表有正序变为倒序）

思路：
①需要找三个指针指定位置左中右做标记
②特殊测试：空链表、只有一个节点的链表
'''

class ListNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

def reverseList(listHead):
    if listHead is None:
        return None
    if listHead.next is None:
        return listHead
    cur1,cur2,cur3 = listHead, listHead.next, listHead.next.next
    
    cur1.next = None

    while cur3 is not None:
        cur2.next = cur1
        cur1 = cur2
        cur2 = cur3
        cur3 = cur3.next

    cur2.next = cur1
    return cur2

# 一般测试
a,b,c,d,e,f,g = ListNode(1),ListNode(2),ListNode(3),ListNode(4),ListNode(5),ListNode(6),ListNode(7)
a.next,b.next,c.next,d.next,e.next,f.next = b,c,d,e,f,g
print(reverseList(a).val)

# 测试空链表
a = None
print(reverseList(a))

# 测试单节点的链表
a = ListNode(1)
print(reverseList(a).val)

