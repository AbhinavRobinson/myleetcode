from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxV = 0
        x = len(height) - 1
        y = 0
        while x != y:
            if height[x] > height[y]:
                area = height[y] * (x - y)
                y += 1
            else:
                area = height[x] * (x - y)
                x -= 1
            maxV = max(maxV, area)
        return maxV
