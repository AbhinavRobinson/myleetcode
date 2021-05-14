'''
Runtime: 480 ms, faster than 83.18% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 49.4 MB, less than 66.12% of Python3 online submissions for Minimum Depth of Binary Tree.
'''

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level+1))
                    queue.append((node.right, level+1))
