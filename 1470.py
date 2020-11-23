class Solution:
    def shuffle(self, nums:[int], n: int) -> [int]:
        output = []
        for i in range(int(len(nums)/2)):
            output.append(nums[i])
            output.append(nums[i+n])
        return output

s = Solution()

nums = [1,2,3,4,4,3,2,1]
n = 4
#Output: [1,4,2,3,3,2,4,1]

print(s.shuffle(nums, n))

"""I can use the parameter n.
So, length of list nums divided by 2 can be used for the 'for loop'
just append i-th element and (i + n)-th element in sequence."""