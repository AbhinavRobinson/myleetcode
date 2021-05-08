'''
Runtime: 368 ms, faster than 42.61% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 21.8 MB, less than 90.00% of Python3 online submissions for Find All Numbers Disappeared in an Array.
'''


class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
        return [i + 1 for i, num in enumerate(nums) if num > 0]
