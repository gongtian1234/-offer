'''
题目：输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是按递增排序的。输出合并后的链表

思路：
建立一个新的链表，找两个游标作为标记, 再找一个指针指向新链表的前一个节点，每次两个游标进行比较从而判断指针的下一个节点
'''
class ListNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None


def merge(pHead1, pHead2):
    if pHead1 is None:
        return pHead2
    elif pHead2 is None:
        return pHead1

    cur1, cur2 = pHead1, pHead2
    newHead = pHead1 if pHead1.val<pHead2.val else pHead2
    newHead = cur1 if cur1.val<cur2.val else cur2
    previousPoint = newHead
    if newHead==cur1:
        cur1 = cur1.next
    else:
        cur2 = cur2.next

    while cur1 is not None and cur2 is not None:
        if cur1.val<cur2.val:
            previousPoint.next = cur1
            previousPoint = cur1    # previousPoint这个位置也要改变
            cur1 = cur1.next
        else:
            previousPoint.next = cur2
            previousPoint.next = cur2
            cur2 = cur2.next

    if cur1 is None:
        previousPoint.next = cur1
    elif cur2 is None:
        previousPoint.next = cur2

    return newHead
