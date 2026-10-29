# Runtime: 18 ms
# Memory: 19.9 MB

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        def f(i, dp):
            if(i >= n):
                return 0

            if(dp[i] != -1):
                return dp[i]
            
            dp[i] = cost[i] + min(f(i+1,dp), f(i+2,dp))
            return dp[i]
        
        dp1 = [-1] * (n+1)
        dp2 = [-1] * (n+1)

        left = f(0, dp1)
        right = f(1, dp2)

        return min(left, right)