class Solution:
    def arrayStringsAreEqual(self, word1: [str], word2: [str]) -> bool:
        word1_concat = ""
        word2_concat = ""
        for i in word1:
            word1_concat += i
        for j in word2:
            word2_concat += j
        # print(word1_concat, word2_concat)
        return (word1_concat == word2_concat)

s = Solution()
print(s.arrayStringsAreEqual(["ab", "c"], ["a", "bc"])) # true
print(s.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"])) # true
