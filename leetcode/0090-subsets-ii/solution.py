# Runtime: 0 ms
# Memory: 19.3 MB

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        arr = []
        nums.sort()

        def f(i, ss=[]):
            if(i == len(nums)):
                arr.append(ss[:])
                return 


            ss.append(nums[i])
            f(i+1, ss)
            ss.pop()

            idx = i+1
            while(idx<len(nums) and nums[idx] == nums[idx-1]):
                idx += 1
            f(idx, ss)
        
        f(0, [])
            
        return arr