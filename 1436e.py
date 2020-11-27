class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        #         dest = []

        #         for j in range(len(paths)):
        #             for i in paths:
        #                 if not dest:
        #                     dest.append(i[-1])
        #                 elif dest[-1] == i[0]:
        #                     dest[0] = i[1]
        #         return dest[0]

        hs = {}

        for x in paths:
            hs[x[0]] = x[1]

        lst = [end for _, end in paths]

        for x in lst:
            if x not in hs:
                return x