'''
Runtime: 916 ms, faster than 97.29% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25 MB, less than 95.30% of Python3 online submissions for Best Time to Buy and Sell Stock.
'''


class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        else:
            low = 99999
            profitmax = 0
            for price in prices:
                if price > low:
                    if price - low > profitmax:
                        profitmax = price - low
                elif price < low:
                    low = price

            return profitmax
