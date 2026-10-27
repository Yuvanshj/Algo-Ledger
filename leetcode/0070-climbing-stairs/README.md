# 70. Climbing Stairs

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Math-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Memoization-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 19.2 MB |
| Submission Date | 2026-10-27T13:44:09.337Z |
| Platform | leetcode |

## Problem Statement

<p>You are climbing a staircase. It takes <code>n</code> steps to reach the top.</p>

<p>Each time you can either climb <code>1</code> or <code>2</code> steps. In how many distinct ways can you climb to the top?</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= n &lt;= 45</code>

## Solution

```py
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        
        def f(i):
            if(i==0):
                return 1
            if(i < 0):
                return 0
            
            if(dp[i] != -1):
                return dp[i]

            dp[i] = f(i-1) + f(i-2)
            return dp[i]

        return f(n)
       
```

[View on LeetCode](https://leetcode.com/problems/climbing-stairs/)
