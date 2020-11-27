class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # output = 0
        # for i in range(1, len(arr) + 1, 2):
        #     for j in range(0, len(arr) - i + 1):
        #         if j+i > len(arr) - 1:
        #             output += sum(arr[j:])
        #         else:
        #             output += sum(arr[j:j+i])
        # return output

        s = 0
        for i in range(len(arr)):
            for j in range(i, len(arr), 2):
                s += sum(arr[i:j + 1])
        return s