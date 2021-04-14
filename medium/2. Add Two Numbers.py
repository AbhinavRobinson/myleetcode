class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        numA,numB = 0,0
        pos = 1
        while l1 != None:
            numA += l1.val * pos
            pos *= 10
            l1 = l1.next
        pos = 1
        while l2 != None:
            numB += l2.val * pos
            pos *= 10
            l2 = l2.next

        lst = [int(i) for i in reversed(str(numA+numB))]
        head = ListNode(lst[0])
        tail = head
        for i in lst[1:]:
            tail.next = ListNode(i)
            tail = tail.next
        return head