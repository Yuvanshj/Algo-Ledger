# Runtime: 13 ms
# Memory: 19.3 MB

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0].append([])

        for i in range(1, target + 1):
            for j in candidates:
                if j <= i:
                    for prev in dp[i - j]:
                        temp = prev + [j]
                        temp.sort()
                        if temp not in dp[i]:
                            dp[i].append(temp)
        return dp[target]
        