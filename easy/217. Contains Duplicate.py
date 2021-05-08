'''
Runtime: 116 ms, faster than 76.43% of Python3 online submissions for Contains Duplicate.
Memory Usage: 20.4 MB, less than 40.06% of Python3 online submissions for Contains Duplicate.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))