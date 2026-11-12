# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 3 ms |
| Memory | 19.2 MB |
| Submission Date | 2026-11-12T16:37:53.727Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an array of integers <code>nums</code>. Return <em>the length of the <strong>longest</strong> <span data-keyword="subarray-nonempty">subarray</span> of </em><code>nums</code><em> which is either <strong><span data-keyword="strictly-increasing-array">strictly increasing</span></strong> or <strong><span data-keyword="strictly-decreasing-array">strictly decreasing</span></strong></em>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,4,3,3,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The strictly increasing subarrays of <code>nums</code> are <code>[1]</code>, <code>[2]</code>, <code>[3]</code>, <code>[3]</code>, <code>[4]</code>, and <code>[1,4]</code>.</p>

<p>The strictly decreasing subarrays of <code>nums</code> are <code>[1]</code>, <code>[2]</code>, <code>[3]</code>, <code>[3]</code>, <code>[4]</code>, <code>[3,2]</code>, and <code>[4,3]</code>.</p>

<p>Hence, we return <code>2</code>.</p>
</div>

<p>
```

**Example 2:**

```
</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,3,3,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The strictly increasing subarrays of <code>nums</code> are <code>[3]</code>, <code>[3]</code>, <code>[3]</code>, and <code>[3]</code>.</p>

<p>The strictly decreasing subarrays of <code>nums</code> are <code>[3]</code>, <code>[3]</code>, <code>[3]</code>, and <code>[3]</code>.</p>

<p>Hence, we return <code>1</code>.</p>
</div>

<p>
```

**Example 3:**

```
</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The strictly increasing subarrays of <code>nums</code> are <code>[3]</code>, <code>[2]</code>, and <code>[1]</code>.</p>

<p>The strictly decreasing subarrays of <code>nums</code> are <code>[3]</code>, <code>[2]</code>, <code>[1]</code>, <code>[3,2]</code>, <code>[2,1]</code>, and <code>[3,2,1]</code>.</p>

<p>Hence, we return <code>3</code>.</p>
</div>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= nums.length &lt;= 50</code>
- <code>1 &lt;= nums[i] &lt;= 50</code>

## Solution

```py
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxLen = 1
        inc = 1
        dec = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1
            maxLen = max(maxLen, inc, dec)
        return maxLen
```

[View on LeetCode](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/)
