# 46. Permutations

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Backtracking-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 19.2 MB |
| Submission Date | 2026-10-26T13:58:05.626Z |
| Platform | leetcode |

## Problem Statement

<p>Given an array <code>nums</code> of distinct integers, return all the possible <span data-keyword="permutation-array">permutations</span>. You can return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre><p>
```

**Example 2:**

```
</p>
<pre><strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> [[0,1],[1,0]]
</pre><p>
```

**Example 3:**

```
</p>
<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> [[1]]
</pre>
<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= nums.length &lt;= 6</code>
- <code>-10 &lt;= nums[i] &lt;= 10</code>
- All the integers of <code>nums</code> are <strong>unique</strong>.

## Solution

```py
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
        
```

[View on LeetCode](https://leetcode.com/problems/permutations/)
