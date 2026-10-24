# Runtime: 0 ms
# Memory: 18.9 MB

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def f(i,ss):
            if(i == len(nums)):
                res.append(ss[:])
                return 
            ss.append(nums[i])
            f(i+1, ss)
            ss.pop()
            f(i+1,ss)
        f(0,[])
        return res