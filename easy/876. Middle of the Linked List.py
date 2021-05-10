'''
Runtime: 32 ms, faster than 45.40% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 14.2 MB, less than 71.12% of Python3 online submissions for Middle of the Linked List.
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast, slow = head, head

        while True:
            if fast.next == None:
                return slow
            if fast.next != None and fast.next.next == None:
                return slow.next

            slow = slow.next
            fast = fast.next.next
