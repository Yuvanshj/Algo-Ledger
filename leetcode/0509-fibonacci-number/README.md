# 509. Fibonacci Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Math-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Recursion-blue) ![Topic](https://img.shields.io/badge/Topic-Memoization-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 358 ms |
| Memory | 19.1 MB |
| Submission Date | 2026-10-24T11:30:27.355Z |
| Platform | leetcode |

## Problem Statement

<p>The <b>Fibonacci numbers</b>, commonly denoted <code>F(n)</code> form a sequence, called the <b>Fibonacci sequence</b>, such that each number is the sum of the two preceding ones, starting from <code>0</code> and <code>1</code>. That is,</p>

<pre>
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n &gt; 1.
</pre>

<p>Given <code>n</code>, calculate <code>F(n)</code>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> F(2) = F(1) + F(0) = 1 + 0 = 1.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> F(3) = F(2) + F(1) = 1 + 1 = 2.
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong> F(4) = F(3) + F(2) = 2 + 1 = 3.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>0 &lt;= n &lt;= 30</code>

## Solution

```py
class Solution:
    def fib(self, n: int) -> int:

        def f(i):
            if(i==0 or i == 1):
                return i
            
            return f(i-1) + f(i-2)
        
        return f(n)

```

[View on LeetCode](https://leetcode.com/problems/fibonacci-number/)
