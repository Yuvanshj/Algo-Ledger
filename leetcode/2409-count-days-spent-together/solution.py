# Runtime: 0 ms
# Memory: 19.2 MB

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

        for i in range(aliceArrMon-1):
            aliceArrTotal += arr[i]
        
        aliceArrTotal += aliceArrDay

        for i in range(aliceLeaveMon-1):
            aliceLeaveTotal += arr[i]
        
        aliceLeaveTotal += aliceLeaveDay

        for i in range(bobArrMon-1):
            bobArrTotal += arr[i]
        
        bobArrTotal += bobArrDay

        for i in range(bobLeaveMon-1):
            bobLeaveTotal += arr[i]
        
        bobLeaveTotal += bobLeaveDay

        
        # print(aliceArrTotal, aliceLeaveTotal, bobArrTotal, bobLeaveTotal)
        start = max(aliceArrTotal, bobArrTotal)
        end = min(aliceLeaveTotal, bobLeaveTotal)

        return max(0, end - start + 1)
