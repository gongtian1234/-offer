# csdn链接：https://blog.csdn.net/xiaotian127/article/details/109246823

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode # 输入和输出都是链表的头节点
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or l2 is None:
            return
        cur1, cur2 = l1, l2
        sign = 0  # 用来标记是否要进一位
        while cur1 is not None or cur2 is not None:
            if cur1 is not None and cur2 is not None:
                now_val = cur1.val + cur2.val + sign
            elif cur1 is not None : # 因为链表可能不一样长，一个已经到末尾，另一个还没有到末尾
                now_val = cur1.val  + sign
            elif cur2 is not None :
                now_val = cur2.val  + sign  
            if cur1 is not None and cur2 is not None and cur1==l1 and cur2==l2:
                if now_val<10:
                    sign = 0
                else:
                    now_val = int(str(now_val)[-1])
                    sign=1
                header = ListNode(val=now_val)
                pre_node = header
            else:
                if now_val <10:
                    sign = 0
                else:
                    now_val = int(str(now_val)[-1])
                    sign = 1
                tmp_node = ListNode(val=now_val)
                pre_node.next = tmp_node
                pre_node = tmp_node
            if cur1 is not None:
                cur1 = cur1.next
            if cur2 is not None:
                cur2 = cur2.next
        if sign==1:  # 如果最后还需要进一位，那么需要新创建一个node节点
            tmp_node = ListNode(val=sign)
            pre_node.next = tmp_node
        return header
                
            
        
        
        
