class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # output = []
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if nums[i] > nums[j]:
        #             count += 1
        #     output.append(count)
        # return output

        hs = {}
        result = []
        for i in nums:
            if i not in hs.keys():
                hs[i] = 1
            else:
                hs[i] += 1
        print(hs)

        for j in nums:
            temp = 0
            for k in hs.keys():
                if j > k:
                    temp += hs[k]
            result.append(temp)

        return result

# The second one using hash table is faster than the another.
