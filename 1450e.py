class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        output = 0
        for i in range(len(startTime)):
            for j in range(startTime[i], endTime[i] + 1):
                if j == queryTime:
                    output += 1
                    break
        return output



    