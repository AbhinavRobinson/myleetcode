'''
Runtime: 60 ms, faster than 95.32% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 17.3 MB, less than 23.79% of Python3 online submissions for Remove Linked List Elements.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:        
#         No head
        if head == None:
            return None
        
#         Head only or Lone Head 
        while head.val == val:
            if head.next == None:
                return None
            head = head.next
                
        slow = head
        fast = head.next
        
#         After Head
        while fast:
            if fast.val != val:
                fast = fast.next
                slow = slow.next
            else:
                fast = fast.next
                slow.next = fast
                
        return head