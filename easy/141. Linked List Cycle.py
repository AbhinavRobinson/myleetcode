'''
Runtime: 60 ms, faster than 20.35% of Python3 online submissions for Linked List Cycle.
Memory Usage: 17.5 MB, less than 74.95% of Python3 online submissions for Linked List Cycle.
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return False

        slow, fast = head, head.next
        while True:
            if fast == slow:
                return True

            if slow.next != None:
                slow = slow.next
            else:
                return False

            if fast.next != None and fast.next.next != None:
                fast = fast.next.next
            else:
                return False
