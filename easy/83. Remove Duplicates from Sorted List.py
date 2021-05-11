'''
Runtime: 44 ms, faster than 48.23% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 14 MB, less than 99.45% of Python3 online submissions for Remove Duplicates from Sorted List.
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        #         no head
        if head == None:
            return None

#         only head
        if head.next == None:
            return head

#         head dupes
        while head.next.val == head.val:
            head = head.next
            if head.next == None:
                return head

        slow = head
        fast = head.next

#         find dupes
        while fast.next:
            if fast.next.val != fast.val:
                fast = fast.next
                slow = slow.next
            else:
                fast = fast.next
                slow.next = fast
        return head
