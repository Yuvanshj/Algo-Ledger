# 78. Subsets

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Backtracking-blue) ![Topic](https://img.shields.io/badge/Topic-Bit_Manipulation-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 18.9 MB |
| Submission Date | 2026-10-24T13:31:09.718Z |
| Platform | leetcode |

## Problem Statement

<p>Given an integer array <code>nums</code> of <strong>unique</strong> elements, return <em>all possible</em> <span data-keyword="subset"><em>subsets</em></span> <em>(the power set)</em>.</p>

<p>The solution set <strong>must not</strong> contain duplicate subsets. Return the solution in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> nums = [0]
<strong>Output:</strong> [[],[0]]
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= nums.length &lt;= 10</code>
- <code>-10 &lt;= nums[i] &lt;= 10</code>
- All the numbers of&nbsp;<code>nums</code> are <strong>unique</strong>.

## Solution

```py
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
```

[View on LeetCode](https://leetcode.com/problems/subsets/)
