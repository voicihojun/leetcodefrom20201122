class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(int(len(nums) / 2)):
            for j in range(nums[2 * i]):
                output.append(nums[2 * i + 1])

        return output