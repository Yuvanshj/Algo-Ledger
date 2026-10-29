# 322. Coin Change

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Breadth--First_Search-blue) ![Topic](https://img.shields.io/badge/Topic-Knapsack_Problem-blue) ![Topic](https://img.shields.io/badge/Topic-Complete_Knapsack-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 1374 ms |
| Memory | 133.6 MB |
| Submission Date | 2026-10-29T19:20:14.521Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an integer array <code>coins</code> representing coins of different denominations and an integer <code>amount</code> representing a total amount of money.</p>

<p>Return the <strong>fewest</strong> number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.</p>

<p>You may assume that you have an infinite number of each kind of coin.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> coins = [1,2,5], amount = 11
<strong>Output:</strong> 3
<strong>Explanation:</strong> 11 = 5 + 5 + 1
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> coins = [2], amount = 3
<strong>Output:</strong> -1
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> coins = [1], amount = 0
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= coins.length &lt;= 12</code>
- <code>1 &lt;= coins[i] &lt;= 2<sup>31</sup> - 1</code>
- <code>0 &lt;= amount &lt;= 10<sup>4</sup></code>

## Solution

```py
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]

        def f(i, amount):
            if amount == 0:
                return 0

            if i < 0:
                return float('inf')

            if dp[i][amount] != -1:
                return dp[i][amount]

            not_take = f(i - 1, amount)

            take = float('inf')

            if coins[i] <= amount:
                take = 1 + f(i, amount - coins[i])

            dp[i][amount] = min(take, not_take)
            return dp[i][amount]

        ans = f(n - 1, amount)

        return -1 if ans == float('inf') else ans

```

[View on LeetCode](https://leetcode.com/problems/coin-change/)
