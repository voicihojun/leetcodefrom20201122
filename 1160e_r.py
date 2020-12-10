from collections import Counter


class Solution:
    def countCharacters(self, words: [str], chars: str) -> int:
        # output = ""
        # for i in words:
        #     char = copy.deepcopy(chars)
        #     for j in range(len(i)):
        #         if i[j] not in chars:
        #             break
        #         if j == len(i) - 1:
        #             output += i
        # print(output)
        # return len(output)

        res = 0
        helper = Counter(chars)
        for i in words:
            count_i = Counter(i)
            for j in set(i):
                if j not in helper:
                    break
                elif j in helper and count_i[j] > helper[j]:
                    break
            else:
                res += len(i)
        return res

        # I learned how to use Counter..