# Runtime: 35 ms
# Memory: 31.9 MB

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        res = -1
        for i in range(len(nums)):
            if nums[i] != i:
                if res == -1:
                    res = nums[i]
                else:
                    res &= nums[i]
        return 0 if res == -1 else res
