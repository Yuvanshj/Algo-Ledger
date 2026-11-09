# Runtime: 31 ms
# Memory: 25.7 MB

class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) != m*n:
            return []

        arr = [[] for _ in range(m)]

        i = 0

        for j in range(m):
            for k in range(n):
                arr[j].append(original[i])
                i += 1
            
        return arr