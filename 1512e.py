"""Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.
"""

class Solution:
    def numIdenticalPairs(self, nums: [int]) -> int:
        output = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    output += 1
        return output

s = Solution()
print(s.numIdenticalPairs([1,2,3,1,1,3])) #4

# I can easily implenment this problem using 2 for loops.

