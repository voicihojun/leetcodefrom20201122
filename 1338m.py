# class Solution:
#     def minSetSize(self, arr: List[int]) -> int:
#         hs = {}
#         for i in arr:
#             if i in hs.keys():
#                 hs[i] += 1
#             else:
#                 hs[i] = 1
#         # print(hs.items())

#         size_of_hs = 0
#         length_half_arr = len(arr) / 2
#         output = 0

#         keys = list(hs.keys())
#         values = list(hs.values())
#         # print(keys)
#         # print(values)
#         # print(values.index(max(values)))

#         while length_half_arr > size_of_hs:
#             size_of_hs += max(values)
#             keys.pop(values.index(max(values)))
#             values.pop(values.index(max(values)))
#             output += 1
#         return output
#   Time limit exceeded

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        hs = {}
        for i in arr:
            if i in hs.keys():
                hs[i] += 1
            else:
                hs[i] = 1
        # print(hs)

        size_of_hs = 0
        length_half_arr = len(arr) / 2
        output = 0

        values = list(hs.values())
        values.sort(reverse=True)

        for i in values:
            size_of_hs += i
            output += 1
            if length_half_arr <= size_of_hs:
                return output

"""I just need to use the values of dict, not the keys of dict. 
To use greedy algo, i need to sort values in descending order, 
and then check if the size of hs is equal or greater than the half length of the arr. """