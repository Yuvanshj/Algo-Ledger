# 2409. Count Days Spent Together

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Math-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 1 ms |
| Memory | 19.1 MB |
| Submission Date | 2026-10-24T11:13:32.782Z |
| Platform | leetcode |

## Problem Statement

<p>Alice and Bob are traveling to Rome for separate business meetings.</p>

<p>You are given 4 strings <code>arriveAlice</code>, <code>leaveAlice</code>, <code>arriveBob</code>, and <code>leaveBob</code>. Alice will be in the city from the dates <code>arriveAlice</code> to <code>leaveAlice</code> (<strong>inclusive</strong>), while Bob will be in the city from the dates <code>arriveBob</code> to <code>leaveBob</code> (<strong>inclusive</strong>). Each will be a 5-character string in the format <code>&quot;MM-DD&quot;</code>, corresponding to the month and day of the date.</p>

<p>Return<em> the total number of days that Alice and Bob are in Rome together.</em></p>

<p>You can assume that all dates occur in the <strong>same</strong> calendar year, which is <strong>not</strong> a leap year. Note that the number of days per month can be represented as: <code>[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]</code>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> arriveAlice = &quot;08-15&quot;, leaveAlice = &quot;08-18&quot;, arriveBob = &quot;08-16&quot;, leaveBob = &quot;08-19&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> arriveAlice = &quot;10-01&quot;, leaveAlice = &quot;10-31&quot;, arriveBob = &quot;11-01&quot;, leaveBob = &quot;12-31&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no day when Alice and Bob are in Rome together, so we return 0.
</pre>

<p>&nbsp;</p>
```

## Constraints

- All dates are provided in the format <code>&quot;MM-DD&quot;</code>.
- Alice and Bob&#39;s arrival dates are <strong>earlier than or equal to</strong> their leaving dates.
- The given dates are valid dates of a <strong>non-leap</strong> year.

## Solution

```py
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        aliceArrMon = int(arriveAlice[0:2])
        aliceArrDay = int(arriveAlice[3:5])

        aliceLeaveMon = int(leaveAlice[0:2])
        aliceLeaveDay = int(leaveAlice[3:5])

        bobArrMon = int(arriveBob[0:2])
        bobArrDay = int(arriveBob[3:5])

        bobLeaveMon = int(leaveBob[0:2])
        bobLeaveDay = int(leaveBob[3:5])

        aliceArrTotal = 0
        aliceLeaveTotal = 0
        bobArrTotal = 0
        bobLeaveTotal = 0

        def giveTotal(total, Day, Mon):
            for i in range(Mon - 1):
                total += arr[i]

            total += Day
            return total

        aliceArrTotal = giveTotal(aliceArrTotal, aliceArrDay, aliceArrMon)
        aliceLeaveTotal = giveTotal(aliceLeaveTotal, aliceLeaveDay, aliceLeaveMon)
        bobArrTotal = giveTotal(bobArrTotal, bobArrDay, bobArrMon)
        bobLeaveTotal = giveTotal(bobLeaveTotal, bobLeaveDay, bobLeaveMon)

        start = max(aliceArrTotal, bobArrTotal)
        end = min(aliceLeaveTotal, bobLeaveTotal)

        return max(0, end - start + 1)
```

[View on LeetCode](https://leetcode.com/problems/count-days-spent-together/)
