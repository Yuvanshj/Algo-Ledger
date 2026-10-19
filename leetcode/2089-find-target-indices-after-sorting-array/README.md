# 2089. Find Target Indices After Sorting Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Binary_Search-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 19.1 MB |
| Submission Date | 2026-10-19T19:49:40.660Z |
| Platform | leetcode |

## Problem Statement

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> and a target element <code>target</code>.</p>

<p>A <strong>target index</strong> is an index <code>i</code> such that <code>nums[i] == target</code>.</p>

<p>Return <em>a list of the target indices of</em> <code>nums</code> after<em> sorting </em><code>nums</code><em> in <strong>non-decreasing</strong> order</em>. If there are no target indices, return <em>an <strong>empty</strong> list</em>. The returned list must be sorted in <strong>increasing</strong> order.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> nums = [1,2,5,2,3], target = 2
<strong>Output:</strong> [1,2]
<strong>Explanation:</strong> After sorting, nums is [1,<u><strong>2</strong></u>,<u><strong>2</strong></u>,3,5].
The indices where nums[i] == 2 are 1 and 2.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> nums = [1,2,5,2,3], target = 3
<strong>Output:</strong> [3]
<strong>Explanation:</strong> After sorting, nums is [1,2,2,<u><strong>3</strong></u>,5].
The index where nums[i] == 3 is 3.
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> nums = [1,2,5,2,3], target = 5
<strong>Output:</strong> [4]
<strong>Explanation:</strong> After sorting, nums is [1,2,2,3,<u><strong>5</strong></u>].
The index where nums[i] == 5 is 4.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= nums.length &lt;= 100</code>
- <code>1 &lt;= nums[i], target &lt;= 100</code>

## Solution

```py
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        arr = []
        for i in range(len(nums)):
            if(nums[i] == target):
                arr.append(i)
        
        return arr
```

[View on LeetCode](https://leetcode.com/problems/find-target-indices-after-sorting-array/)
