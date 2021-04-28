'''
Runtime: 32 ms, faster than 79.30% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 14.2 MB, less than 56.07% of Python3 online submissions for String to Integer (atoi).
'''


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        # empty ?
        if len(s) == 0:
            return 0

        # is negative ?
        neg = 1
        if s[0] == '-':
            neg = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # Is anything left ?
        if len(s) == 0 or s == '':
            return 0

        # Is it a number ?
        if s[0] in "0123456789":
            builder = ''
            for i in s:
                if i == ' ' or i == '' or i not in "0123456789":
                    break
                # concat
                builder += i
            if builder != '':
                res = int(builder)
                # is it over limit ?
                if neg > 0 and res >= 2147483647:
                    return 2147483647
                elif res >= 2147483648:
                    return -1*2147483648
                return res * neg
        return 0
