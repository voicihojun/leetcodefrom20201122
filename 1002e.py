class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        hs = {}
        output = []
        for i in A[0]:
            if i not in hs.keys():
                hs[i] = 1
            else:
                hs[i] += 1
        for i in range(1,len(A)):
            for j in hs.keys():
                if A[i].count(j) == 0:
                    hs[j] = 0
                elif A[i].count(j) < hs[j]:
                    hs[j] = A[i].count(j)
        for k,v in hs.items():
            if(v > 0):
                for i in range(v):
                    output.append(k)
        # print(output)
        return output

