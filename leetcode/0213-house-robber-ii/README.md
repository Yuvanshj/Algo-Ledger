# 213. House Robber II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 19.1 MB |
| Submission Date | 2026-10-28T19:19:42.495Z |
| Platform | leetcode |

## Problem Statement

<p>You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are <strong>arranged in a circle.</strong> That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and&nbsp;<b>it will automatically contact the police if two adjacent houses were broken into on the same night</b>.</p>

<p>Given an integer array <code>nums</code> representing the amount of money of each house, return <em>the maximum amount of money you can rob tonight <strong>without alerting the police</strong></em>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> nums = [2,3,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= nums.length &lt;= 100</code>
- <code>0 &lt;= nums[i] &lt;= 1000</code>

## Solution

```py
class Solution:
    def rob(self, nums: list[int]) -> int:

        def f(i, n, dp):

            if(i >= n):
                return 0
            
            if(dp[i]!= -1):
                return dp[i]
            
            pick = nums[i] + f(i+2,n, dp)
            not_pick = f(i+1,n, dp)

            dp[i] = max(pick , not_pick)
            return dp[i]
        
        if len(nums) == 1:
            return nums[0]
        
        dp1 = [-1] * (len(nums)+1)
        fs = f(0, len(nums)-1, dp1)

        dp2 = [-1] * (len(nums)+1)
        sd = f(1,len(nums), dp2)

        return max(fs, sd)
```

[View on LeetCode](https://leetcode.com/problems/house-robber-ii/)
