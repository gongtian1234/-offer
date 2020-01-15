'''
面试题22：输入一个(单向)链表，输出该链表中倒数第k个节点。如链表为[1,2,3,4,5], k=2时，输出倒数第二个节点为4

思路：
①先遍历一次列表获得链表的长度n，再从头遍历到n-k+1个值，输出即可，但是这样时间复杂度高
②找两个指针cur1(第i个位置)、cur2(第i+k个位置)，并另二者的间隔为k，当cur2走到链表尾部时，cur1所指的就是倒数第k个值。【注意：输入的链表为空或者
链表的长度小于k时，会直接报错】
③防爆措施：1、当输入的k小于1时，返回None；2、链表为空，返回None；3、链表长度小于k，返回None
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def findKthToTail(head, k):
    if (head.val is None and head.next is None) or k<1:
        return 

    cur1 = head
    cur2 = head
    for i in range(k-1):    # 先让指针cur2指向cur1的前k个节点
        if cur2.next is None:   # 当链表的长度小于k时
            return 
        print('0',cur2.val)
        cur2 = cur2.next
        print('1',cur2.val)
    while cur2.next is not None:
        cur2 = cur2.next
        cur1 = cur1.next

    return cur1.val

a,b,c,d,e,f,g = ListNode(1),ListNode(2),ListNode(3),ListNode(4),ListNode(5),ListNode(6),ListNode(7)
a.next,b.next,c.next,d.next,e.next,f.next = b,c,d,e,f,g

print(findKthToTail(a, 1))
