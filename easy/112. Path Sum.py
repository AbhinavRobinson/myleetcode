'''
Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Runtime: 32 ms, faster than 98.32% of Python3 online submissions for Path Sum.
Memory Usage: 15.8 MB, less than 89.08% of Python3 online submissions for Path Sum.
'''
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        queue = deque([(root, root.val)])
        while queue:
            node, val = queue.popleft()
            if node:
                if not node.left and not node.right:
                    if val == targetSum:
                        return True
                else:
                    if node.left:
                        queue.append((node.left, val+node.left.val))
                    if node.right:
                        queue.append((node.right, val+node.right.val))
        return False
