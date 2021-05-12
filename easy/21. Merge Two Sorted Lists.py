'''
Runtime: 32 ms, faster than 90.12% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.3 MB, less than 61.48% of Python3 online submissions for Merge Two Sorted Lists.
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode()
        ptr = root
        while l1 and l2:
            if l1.val < l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next
        if l1:
            ptr.next = l1
        elif l2:
            ptr.next = l2

        return root.next
