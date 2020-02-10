'''
题目：给定一个链表，若其中包含环，请找出该链表的环的入口节点，否则输出null

思路：
①找一个set，记录下环中的每一个节点，如果遇到None，则无环，如果再次遇到相同的节点，则表明有环，且该该节点为环的入口节点；
②（先判断是否有环，无环则return None，有环再去寻找环的入口）找两个指针fastPointer、slowPointer，f每次走两步，s每次只走一步，如果f
遇到none表明无环，否则有环（注意当f==s时，说明，f在环里面追上了s，表明有环）；在判断环的入口位置，经过数学公式证明，当两个指针在环
中第一次相遇后，此时找一个新的指针从头开始一步一步移动，s也一步一步往前移，二者相遇的位置就是入口节点
证明过程如下（假设链表中有环）：
假设s与f第一次相遇时，s已经走了l步，则f走了2l步；
假设入环前的步长为a，s进环后与f相遇又走了b步，则l=a+b，相遇的位置距离环的入口为c; 
则f所走的步长2l=a+n*(b+c)+b, 其中n表示f在环中所绕的圈数
有2*(a+b)=a+n*(b+c)+b, 化简得a=c+(n-1)*(b+c),（其中b+c表示环的长度）

'''
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


def entryNodeOfLoop(pHead):
    if pHead is None:
        return None

    fastPointer, slowPointer = pHead, pHead
    
    while fastPointer is not None and fastPointer.next is not None:
        fastPointer = fastPointer.next.next
        slowPointer = slowPointer.next
        if fastPointer == slowPointer:
            break

    if fastPointer is None or fastPointer.next is None:
        return None

    fastPointer = pHead
    while fastPointer!=slowPointer:
        fastPointer = fastPointer.next
        slowPointer = slowPointer.next
    return fastPointer

if __name__=='__main__':
    # 测试一般的普通情况
    a, b, c, d, e = ListNode(1),ListNode(2),ListNode(3),ListNode(4),ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = c
    print('环的入口节点为：',entryNodeOfLoop(a).val)

    # 测试空链表
    print('空链表进行测试：',entryNodeOfLoop(None))

    # 无环链表进行测试
    a, b, c, d, e = ListNode(1),ListNode(2),ListNode(3),ListNode(4),ListNode(5)
    a.next,b.next, c.next, d.next = b, c, d, e
    print('无环链表进行测试:',entryNodeOfLoop(a))


