class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        #         hs = {}
        #         for i in arr:
        #             if i not in hs.keys():
        #                 hs[i] = 1
        #             else:
        #                 hs[i] +=1
        #         print(hs)
        #         arr_set = set(arr)
        #         print(arr_set)
        #         output = []
        #         for i in arr_set:
        #             output.append(hs[i])
        #         print(output)
        #         return len(output) == len(set(output))

        s = list(set(arr))
        d = set()
        for i in s:
            count = arr.count(i)
            d.add(count)
        return len(d) == len(s)

# Using set and list, the problem can be easily implemented.