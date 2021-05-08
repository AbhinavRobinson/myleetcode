'''
Runtime: 120 ms, faster than 95.91% of Python3 online submissions for Missing Number.
Memory Usage: 15.4 MB, less than 80.67% of Python3 online submissions for Missing Number.
'''


class Solution:
    def missingNumber(self, nums):
        return int(len(nums)*(len(nums)+1)/2 - sum(nums))
