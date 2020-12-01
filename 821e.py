class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        #         c_position = []
        #         for idx in range(len(S)):
        #             if S[idx] == C:
        #                 c_position.append(idx)
        #         output = []

        #         for i in range(len(S)):
        #             minimum = []
        #             for j in c_position:

        #                 minimum.append(abs(i - j))
        #             output.append(min(minimum))

        #         return output

        c_position = []
        for idx in range(len(S)):
            if S[idx] == C:
                c_position.append(idx)
        output = []
        for i in range(len(S)):
            output.append(min([abs(i - j) for j in c_position]))

        return output