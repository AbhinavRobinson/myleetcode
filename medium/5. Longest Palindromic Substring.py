class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            odd = self.grow(s,i,i)
            if len(odd) > len(ans):
                ans = odd
            even = self.grow(s,i,i+1)
            if len(even) > len(ans):
                ans = even
                
        return ans
    
    def grow(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l-=1
            r+=1
        return s[l+1:r]