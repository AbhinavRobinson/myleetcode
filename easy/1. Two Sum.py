from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inda, indb = -1,-1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i]+nums[j] == target:
                    inda, indb = i,j
        return [indb,inda]