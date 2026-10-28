# Runtime: 1 ms
# Memory: 19.3 MB

class Solution:
    def rob(self, nums: list[int]) -> int:

        def f(i, n, dp):

            if(i >= n):
                return 0
            
            if(dp[i]!= -1):
                return dp[i]
            
            pick = nums[i] + f(i+2,n, dp)
            not_pick = f(i+1,n, dp)

            dp[i] = max(pick , not_pick)
            return dp[i]
        
        if len(nums) == 1:
            return nums[0]
        
        dp1 = [-1] * (len(nums)+1)
        fs = f(0, len(nums)-1, dp1)

        dp2 = [-1] * (len(nums)+1)
        sd = f(1,len(nums), dp2)

        return max(fs, sd)