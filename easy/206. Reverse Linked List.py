'''
Runtime: 32 ms, faster than 85.46% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.7 MB, less than 42.71% of Python3 online submissions for Reverse Linked List.
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
