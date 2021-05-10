'''
Runtime: 668 ms, faster than 96.34% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 31.3 MB, less than 98.17% of Python3 online submissions for Palindrome Linked List.
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        reverser = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            reverser, reverser.next, slow = slow, reverser, slow.next

        # on even case
        if fast:
            slow = slow.next

        while reverser and reverser.val == slow.val:
            slow = slow.next
            reverser = reverser.next

        # if reverser none, means traversed full list, ie, palindrome
        return not reverser
