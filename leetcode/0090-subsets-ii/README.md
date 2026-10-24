# 90. Subsets II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Backtracking-blue) ![Topic](https://img.shields.io/badge/Topic-Bit_Manipulation-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 19.3 MB |
| Submission Date | 2026-10-24T14:11:05.629Z |
| Platform | leetcode |

## Problem Statement

<p>Given an integer array <code>nums</code> that may contain duplicates, return <em>all possible</em> <span data-keyword="subset"><em>subsets</em></span><em> (the power set)</em>.</p>

<p>The solution set <strong>must not</strong> contain duplicate subsets. Return the solution in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<pre><strong>Input:</strong> nums = [1,2,2]
<strong>Output:</strong> [[],[1],[1,2],[1,2,2],[2],[2,2]]
</pre><p>
```

**Example 2:**

```
</p>
<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> [[],[0]]
</pre>
<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= nums.length &lt;= 10</code>
- <code>-10 &lt;= nums[i] &lt;= 10</code>

## Solution

```py
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
```

[View on LeetCode](https://leetcode.com/problems/subsets-ii/)
