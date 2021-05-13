'''
Runtime: 236 ms, faster than 59.72% of Python3 online submissions for Binary Search.
Memory Usage: 15.7 MB, less than 27.63% of Python3 online submissions for Binary Search.
'''

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l <= r:
            m = (l + r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1 