class Solution:
    def reverse(self, x: int) -> int:
        rev = int(str(x)[::-1]) if x >= 0 else int('-'+(str(x)[1:])[::-1]) 
        return 0 if abs(rev) > 2147483647 else rev