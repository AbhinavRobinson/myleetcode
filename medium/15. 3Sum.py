'''
Runtime: 848 ms, faster than 74.26% of Python3 online submissions for 3Sum.
Memory Usage: 17 MB, less than 97.07% of Python3 online submissions for 3Sum.
'''

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        #sort
        nums.sort()
        for i in range(len(nums)-2):
            # same as last
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # start at edges 
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    # too negative
                    l +=1 
                elif s > 0:
                    # too positive
                    r -= 1
                else:
                    # at 0
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        # skip same 
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        # skip same                        
                        r -= 1
                    l += 1; r -= 1
        return res