from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, min_price = 0, float('inf')
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > profit:
                profit = price - min_price

        return profit


