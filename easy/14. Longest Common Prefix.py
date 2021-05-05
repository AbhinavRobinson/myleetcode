'''
Runtime: 40 ms, faster than 18.51% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14.2 MB, less than 82.21% of Python3 online submissions for Longest Common Prefix.
'''


from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pfx = ''
        for i in range(200):
            if len(strs[0]) < i+1 or strs[0] == "":
                break
            curr = strs[0][i]
            for j in range(len(strs)):
                if len(strs[j]) < i+1 or strs[j] == "":
                    return pfx
                if strs[j][i] != curr:
                    return pfx
            pfx += curr
        return pfx
