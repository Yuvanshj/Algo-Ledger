# Runtime: 0 ms
# Memory: 19.3 MB

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * (n+1)

        def f(i):

            if i == n:
                return 1

            if s[i] == '0':
                return 0
            
            if(dp[i] != -1):
                return dp[i]

            res = f(i + 1)

            if i + 1 < n and (
                s[i] == '1' or
                (s[i] == '2' and s[i + 1] in '0123456')
            ):
                res += f(i + 2)
            
            dp[i] = res
            return res

        return f(0)