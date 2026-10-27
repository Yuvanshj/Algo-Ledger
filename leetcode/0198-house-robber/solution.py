# Runtime: 0 ms
# Memory: 19.4 MB

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * (len(nums)+1)

        def f(i):
            if i >= len(nums):
                return 0
            
            if(dp[i] != -1):
                return dp[i]

            pick = nums[i] + f(i + 2)
            not_pick = f(i + 1)

            dp[i] = max(pick, not_pick)
            return dp[i]

        return f(0)