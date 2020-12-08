import copy
class Solution:
    #     def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
    #         numerator = 0
    #         denominator = 0

    #         output = copy.deepcopy(M)

    #         for i in range(len(M)):
    #             for j in range(len(M[0])):
    #                 denominator += 1
    #                 numerator += M[i][j]

    #                 if j-1 >= 0:
    #                     denominator += 1
    #                     numerator += M[i][j-1]
    #                     if i-1 >= 0:
    #                         denominator += 1
    #                         numerator += M[i-1][j-1]
    #                     if i+1 < len(M):
    #                         denominator += 1
    #                         numerator += M[i+1][j-1]

    #                 if j+1 < len(M[0]):
    #                     denominator += 1
    #                     numerator += M[i][j+1]
    #                     if i-1 >= 0:
    #                         denominator += 1
    #                         numerator += M[i-1][j+1]
    #                     if i+1 < len(M):
    #                         denominator += 1
    #                         numerator += M[i+1][j+1]

    #                 if i-1 >= 0:
    #                     denominator += 1
    #                     numerator += M[i-1][j]

    #                 if i+1 < len(M):
    #                     denominator += 1
    #                     numerator += M[i+1][j]

    #                 output[i][j] = floor(numerator / denominator)

    #         return output
    # time limite

    def imageSmoother(self, M: [[int]]) -> [[int]]:
        n = len(M)
        m = len(M[0])
        M2 = copy.deepcopy(M)
        for i in range(n):
            M[i].append(-1)
        M.append([-1] * (m + 1))
        for i in range(n):
            for j in range(m):
                tmp = [M[i - 1][j - 1], M[i][j - 1], M[i + 1][j - 1], M[i - 1][j], M[i + 1][j], M[i - 1][j + 1],
                       M[i][j + 1], M[i + 1][j + 1]]
                c = tmp.count(-1)
                M2[i][j] += sum(tmp) + c
                M2[i][j] = int(M2[i][j] / (9 - c))
        return M2