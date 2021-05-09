'''
Runtime: 56 ms, faster than 97.17% of Python3 online submissions for Maximum Subarray.
Memory Usage: 14.9 MB, less than 78.76% of Python3 online submissions for Maximum Subarray.
'''


class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]

        maxSum = res = nums[0]

        for i in range(1, len(nums)):
            res = nums[i] if nums[i] > res + nums[i] else res + nums[i]
            if res > maxSum:
                maxSum = res

        return maxSum
