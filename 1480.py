class Solution:
    def runningSum(self, nums):
        result = []
        for idx in range(len(nums)):
            if idx == 0:
                result.append(nums[idx])
            else:
                result.append(nums[idx] + result[idx - 1])
        return result

nums = [1,2,3,4] # [1,3,6,10]

s = Solution()
print(s.runningSum(nums))
