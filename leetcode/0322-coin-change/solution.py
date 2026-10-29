# Runtime: 1374 ms
# Memory: 133.6 MB

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]

        def f(i, amount):
            if amount == 0:
                return 0

            if i < 0:
                return float('inf')

            if dp[i][amount] != -1:
                return dp[i][amount]

            not_take = f(i - 1, amount)

            take = float('inf')

            if coins[i] <= amount:
                take = 1 + f(i, amount - coins[i])

            dp[i][amount] = min(take, not_take)
            return dp[i][amount]

        ans = f(n - 1, amount)

        return -1 if ans == float('inf') else ans
