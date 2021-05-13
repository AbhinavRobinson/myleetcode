'''
Runtime: 108 ms, faster than 58.17% of Python3 online submissions for Find Smallest Letter Greater Than Target.
Memory Usage: 14.3 MB, less than 82.97% of Python3 online submissions for Find Smallest Letter Greater Than Target.
'''

from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]

        l, r = 0, len(letters)-1
        while l < r:
            m = (l + r)//2
            if letters[m] <= target:
                l = m + 1
            else:
                r = m
        return letters[l % len(letters)]
