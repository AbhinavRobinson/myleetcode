'''
Runtime: 72 ms, faster than 78.18% of Python3 online submissions for Peak Index in a Mountain Array.
Memory Usage: 15.4 MB, less than 53.82% of Python3 online submissions for Peak Index in a Mountain Array.
'''

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1
        while l <= r:
            m = (l+r)//2
            if arr[m] > arr[m-1] and arr[m] > arr[m+1]:
                return m
            elif (m != 0 and arr[m] > arr[m-1]) and (m != len(arr)-1 and arr[m] < arr[m+1]):
                l = m+1
            elif (m != 0 and arr[m] < arr[m-1]) and (m != len(arr)-1 and arr[m] > arr[m+1]):
                r = m-1
            elif arr[m] > arr[-1] and arr[m] < arr[m+1]:
                l = m+1
            else:
                r = m-1
