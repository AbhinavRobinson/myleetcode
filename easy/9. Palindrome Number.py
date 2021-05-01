'''
Runtime: 52 ms, faster than 87.06% of Python3 online submissions for Palindrome Number.
Memory Usage: 14.2 MB, less than 76.92% of Python3 online submissions for Palindrome Number.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0): return False
        if (x > 0 and x%10 == 0): return False
        x = str(x)
        return True if x[::-1] == x else False