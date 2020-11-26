from collections import defaultdict

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        #         word = defaultdict(int)
        #         for i in range(len(indices)):
        #             word[indices[i]] = s[i]
        #         print(word)

        #         output = ""
        #         for i in range(len(indices)):
        #             output += word[i]
        #         return output

        return ''.join([s[indices.index(i)] for i in range(len(s))])

# The commented one that I did is the same performance as the single line one.