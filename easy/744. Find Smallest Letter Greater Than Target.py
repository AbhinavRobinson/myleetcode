'''
Runtime: 104 ms, faster than 81.51% of Python3 online submissions for Find Smallest Letter Greater Than Target.
Memory Usage: 14.6 MB, less than 37.16% of Python3 online submissions for Find Smallest Letter Greater Than Target.
'''

from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Wrap Around
        if target >= letters[-1]:
            return letters[0]

        l, r = 0, len(letters)-1
        while l < r:
            m = (l+r)//2
            if letters[m] > target:
                r = m
            else:
                l = m + 1
        return letters[l]
