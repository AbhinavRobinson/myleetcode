'''
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Runtime: 36 ms, faster than 96.06% of Python3 online submissions for Diameter of Binary Tree.
Memory Usage: 16.3 MB, less than 48.85% of Python3 online submissions for Diameter of Binary Tree.
'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        self.maxDiameter = 0

        def _diameter(node, diameter):
            if node:
                diameter += 1
                if not node.left and not node.right:
                    return 1
                if (node.left or node.right) and (not node.left and not node.right):
                    return _diameter(node.left, diameter) if node.left else _diameter(node.right, diameter)

                ldia, rdia = _diameter(node.left, diameter), _diameter(
                    node.right, diameter)
                self.maxDiameter = max(self.maxDiameter, rdia+ldia)
                return max(rdia, ldia) + 1
            return 0

        _diameter(root, 0)
        return self.maxDiameter
