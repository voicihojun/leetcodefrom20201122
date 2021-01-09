class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        dic = {}
        C = A + " " + B

        for i in C.split():
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1

        return [i for i, v in dic.items() if v == 1]
