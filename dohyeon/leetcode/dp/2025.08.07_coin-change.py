from typing import List


class Solution:
    def coinChange_greedy(self, coins: List[int], amount: int) -> int:
        """Greedy Algorithm"""
        count = 0
        if amount < 0:
            return 0
        sorted_coin = sorted(coins, reverse=True)
        for coin in sorted_coin:
            count += amount // coin
            amount -= (amount // coin) * coin

        return count if amount == 0 else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        """Dynamic Programming"""
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

solution = Solution()
coins = [2]
amount = 3

print(solution.coinChange_greedy(coins, amount))