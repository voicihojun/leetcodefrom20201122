import numpy as np


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        data = np.array(mat)
        output = 0
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == 1 and sum(data[i]) == 1 and sum(data.T[j]) == 1:
                    output += 1

        return output