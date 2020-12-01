class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        output = []
        nums.sort(reverse=True)
        # print(nums)
        while sum(output) <= sum(nums):
            output.append(nums.pop(0))

        return output