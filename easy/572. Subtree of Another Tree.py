# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root 
# with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
# The tree tree could also be considered as a subtree of itself.
# 
# Runtime: 148 ms, faster than 76.78% of Python3 online submissions for Subtree of Another Tree.
# Memory Usage: 14.9 MB, less than 87.38% of Python3 online submissions for Subtree of Another Tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if self.hasSubRoot(root,subRoot):
            return True
        if not root:
            return False
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
    
    def hasSubRoot(self, root, subRoot):
        if not (root and subRoot):
            return root is subRoot
        return (root.val == subRoot.val and 
            self.hasSubRoot(root.left, subRoot.left) and 
            self.hasSubRoot(root.right, subRoot.right))