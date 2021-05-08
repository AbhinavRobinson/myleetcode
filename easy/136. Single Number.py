'''
Runtime: 128 ms, faster than 82.12% of Python3 online submissions for Single Number.
Memory Usage: 16.7 MB, less than 59.82% of Python3 online submissions for Single Number.
'''


class Solution:
    def singleNumber(self, nums):
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]
