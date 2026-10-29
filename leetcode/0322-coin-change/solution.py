# Runtime: 465 ms
# Memory: 19.5 MB

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)
        # dp = [-1] * (n+1)

        # def f(i, amount):
        #     if(amount == 0):
        #         return 0
            
        #     if(i < 0):
        #         return float('inf')

        #     if(dp[i] != -1):
        #         return dp[i]
            
        #     not_take = f(i-1, amount)

        #     take = float('inf')

        #     if(coins[i] <= amount):
        #         take = 1 + f(i, amount - coins[i])

        #     dp[i] = min(take, not_take)
        #     return dp[i]
        
        # ans = f(n-1, amount)

        # return -1 if ans == float('inf') else ans

        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if(coin <= i):
                    dp[i] = min(dp[i], 1+dp[i-coin])
        
        return dp[amount] if dp[amount] != float('inf') else -1