'''
题目一：在O(1)时间内删除列表节点，返回最终链表的头节点。给定单向列表的头指针和一个节点指针，定义一个函数在O(1)时间内删除该节点。

思路：
因为最终要返回的是链表的头节点，所以需要借助空间复制一个新的链表，但是新的链表比原链表的在头节点处多一个元素，然后接下来的操作在新链表上进行，
最终返回新链表的next。需要借助两个指针用来标记前后位置，如果前面的节点发现了目标节点，则后面的指针指向前面节点的下一个节点，从而实现删除节点；
要注意删除节点不存在的情况

题目二：删除链表中的重复节点。在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链
表1->2->3->3->4->4->5 处理后为 1->2->5

思路：
因为最终要返回的是链表的头节点，所以需要借助空间复制一个新的链表，但是新的链表比原链表的在头节点处多一个元素，然后接下来的操作在新链表上进行，
最终返回新链表的next。需要借助两个指针用来标记前后位置，先找到重复的节点的值，然后再去删除从该节点起等于删除节点值的节点
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, pHead, pToBeDeleted):
        ''' 删除链表的节点，并返回头节点，链表中无重复值 '''
        if pHead is None or pToBeDeleted is None:
            return pHead
        bHead = ListNode(pHead.val-1)
        bHead.next = pHead
        cur = pHead    # 标记当前位置
        preCur = bHead
        isFind = 0     # 标记是否找到，找到为1，否则为0
        while cur is not None:
            if cur == pToBeDeleted:
                isFind = 1
                preCur.next = cur.next
                break
            else:
                preCur = cur
                cur = cur.next
        # print(isFind)
        if isFind==1:
            return bHead.next
        else:
            return 'No find deleteNode in pHead!'

if __name__ == '__main__':
    l1,l2,l3,l4 = ListNode(1),ListNode(2),ListNode(3),ListNode(4)
    l1.next, l2.next, l3.next = l2, l3, l4
    l5 = ListNode(5)
    s = Solution()
    # 删除尾节点
    # print(s.deleteNode(l1,l4).next.next.next)
    # 要删除的节点不在链表里面, 此时返回的是提示语
    # print(s.deleteNode(l1,l5))
    # 删除头节点
    print(s.deleteNode(l5,l5))



# class Solution2:
#     def deleteDuplication(self, pHead):
#         ''' 删除链表中的重复节点 '''
#         if pHead is None or pHead.next is None:
#             return pHead
#         bHead = ListNode(pHead.val-1)
#         bHead.next = pHead
#         firstNode = bHead
#         secondHead = pHead
#         while secondHead is not None and secondHead.next is not None:
#             if secondHead.val == secondHead.next.val:
#                 delVal = secondHead.val
#                 while secondHead is not None and (secondHead.val==delVal):
#                     secondHead = secondHead.next
#                 firstNode.next = secondHead
#             else:
#                 firstNode = firstNode.next
#                 secondHead = secondHead.next
#         return bHead.next


