# Runtime: 0 ms
# Memory: 19.1 MB

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        arr = []
        for i in range(len(nums)):
            if(nums[i] == target):
                arr.append(i)
        
        return arr