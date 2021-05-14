'''
Runtime: 44 ms, faster than 90.48% of Python3 online submissions for Average of Levels in Binary Tree.
Memory Usage: 17.3 MB, less than 10.71% of Python3 online submissions for Average of Levels in Binary Tree.
'''

from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []

        info = []

        def dfs(node, depth=0):
            if node:
                if len(info) <= depth:
                    info.append([])
                info[depth].append(node.val)
                dfs(node.right, depth+1)
                dfs(node.left, depth+1)
        dfs(root)
        return [sum(i)/len(i) for i in info]
