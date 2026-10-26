# Runtime: 0 ms
# Memory: 19.2 MB

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def getPerms(nums, idx, ans):
            if idx == len(nums):
                ans.append(nums[:])
                return

            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]

                getPerms(nums, idx + 1, ans)

                nums[idx], nums[i] = nums[i], nums[idx]

        getPerms(nums, 0, ans)
        return ans
        