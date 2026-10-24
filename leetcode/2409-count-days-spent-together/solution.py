# Runtime: 1 ms
# Memory: 19.1 MB

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