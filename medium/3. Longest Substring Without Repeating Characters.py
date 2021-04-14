class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chosen = ''
        max_size = 0
        for i in s:
            if i not in chosen:
                chosen += i
            else:
                chosen = chosen[chosen.index(i)+1:]+i
            max_size = len(chosen) if len(chosen) >= max_size else max_size
        return max_size