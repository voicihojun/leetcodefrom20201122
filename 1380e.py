class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        lucky = []
        for i in matrix:
            print(i)
            row_min = min(i)
            for j in zip(*matrix):
                print(j)
                col_max = max(j)
                if row_min == col_max:
                    lucky.append(row_min)
        return lucky

# how to use zip(*iterable)
"""for example,

[[3, 7, 8], [9, 11, 13], [15, 16, 17]]

[3, 7, 8]
[9, 11, 13]
[15, 16, 17]

(3, 9, 15)
(7, 11, 16)
(8, 13, 17)
"""
