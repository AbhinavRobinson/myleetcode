'''
Runtime: 72 ms, faster than 92.36% of Python3 online submissions for Range Sum Query - Immutable.
Memory Usage: 17.8 MB, less than 20.80% of Python3 online submissions for Range Sum Query - Immutable.
'''


class NumArray(object):
    def __init__(self, nums):
        self.dp = nums
        for i in range(1, len(nums)):
            self.dp[i] += self.dp[i-1]

    def sumRange(self, i, j):
        return self.dp[j] - (self.dp[i-1] if i > 0 else 0)
