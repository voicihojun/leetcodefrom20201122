class Solution:
    def groupThePeople(self, groupSizes: [int]) -> [[int]]:
        s1 = set(groupSizes)
        l1 = list(s1)
        l2 = []
        for i in l1:
            num = 0
            for j in range(len(groupSizes)):
                if (i == groupSizes[j]):
                    num = num + 1
            l2.append(int(num / i))

        outputs = []
        for i in l1:
            output = []
            for j in range(len(groupSizes)):
                if (i == groupSizes[j]):
                    output.append(j)
            outputs.append(output)
        # print(outputs, l1, l2)

        for k in range(len(outputs)):
            if (len(outputs[k]) != l1[k]):
                divide = [outputs[k][idx * l1[k]:(idx + 1) * l1[k]] for idx in range(len(outputs[k]) // l1[k])]
                # print(divide)
                for l in divide:
                    outputs.append(l)
                    # print(outputs)
                # print(outputs)
            else:
                outputs.append(outputs[k])
                # print(outputs)
        return outputs[len(l1):]


"""another person's solution. This is more elegant and easier to read
   I learn about the dict, enumerate. 
   there is no many difference between memory usages, but this one(68 ms) is much faster than mine(88 ms)
   My way to solve this problem is, 
   first of all, find the sort of the element of groupSize when using set. 
   For example, [3,3,3,3,3,1,3], this list has 3 or 1 as element.
   and then when using for loops, we can recognize the index for 3 or 1. 
   so, the result will be [[5], [0,1,2,3,4,6]]. But length of [0,1,2,3,4,6] is 6, not 3. 
   finally, i need to make it divide into 2 group as ,for example, [0,1,2], [3,4,6]. """
# class Solution:
#     def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
#         grp = defaultdict(list)
#         ans = []
#
#         for pid, size in enumerate(groupSizes):
#             grp[size].append(pid)
#             print(grp, ans)
#             if len(grp[size]) == size:
#                 ans.append(grp[size])
#                 grp[size] = []
#         return ans

s = Solution()
print(s.groupThePeople([3,4,3,3,4,4,3,4,3,3]))