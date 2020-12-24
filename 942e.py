class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        increase = 0
        decrease = len(S)
        output = []
        for i in S:
            if i == 'I':
                output.append(increase)
                increase += 1
            else:
                output.append(decrease)
                decrease -= 1
        output.append(increase)

        return output