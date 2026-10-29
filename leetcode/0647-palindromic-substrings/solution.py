# Runtime: 782 ms
# Memory: 19.3 MB

class Solution:
    def countSubstrings(self, s: str) -> int:
    
        n = len(s)
        c = 0

        for i in range(n):
            for j in range(i + 1, n + 1):
                if(s[i:j] == s[i:j][::-1]):
                    c += 1
        
        return c
        
            
    