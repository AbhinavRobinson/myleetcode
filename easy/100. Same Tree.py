'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


Runtime: 24 ms, faster than 94.19% of Python3 online submissions for Same Tree.
Memory Usage: 14.2 MB, less than 85.17% of Python3 online submissions for Same Tree.
'''

# Definition for a binary tree node.

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        queue = deque([(p, q)])
        while queue:
            p, q = queue.popleft()
            if (p or q) and (not p or not q or p.val != q.val):
                return False
            else:
                if p and q:
                    queue.append((p.left, q.left))
                    queue.append((p.right, q.right))
        return True
