'''
Runtime: 48 ms, faster than 68.12% of Python3 online submissions for Integer to Roman.
Memory Usage: 14.3 MB, less than 56.91% of Python3 online submissions for Integer to Roman.
'''


class Solution:
    def intToRoman(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC",
                    "L", "XL", "X", "IX", "V", "IV", "I"]
        res = ""
        for i, v in enumerate(values):
            res += (num//v) * numerals[i]
            num %= v
        return res
