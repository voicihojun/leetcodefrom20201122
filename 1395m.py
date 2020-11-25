from itertools import combinations

class Solution:
    def numTeams(self, rating: [int]) -> int:
        l1 = list(combinations(rating, 3))
        original = []
        for i in l1:
            original.append(list(i))

        output = 0
        for idx, element in enumerate(original):
            if (element[0] < element[1] < element[2]) or (element[0] > element[1] > element[2]):
                output += 1

        return output

s = Solution()
print(s.numTeams([2,5,3,4,1])) # 3 / [2,3,4], [5,3,1], [5,4,1]

"""Using combinations, i am able to obtain the combinations of list. 
For example, for the list [2,5,3,4],
I can have [[2,5,3], [2,5,4], [2,3,4], [5,3,4]]
Then, if the each inside list is ascending or descending order, output is added by 1. 
"""
