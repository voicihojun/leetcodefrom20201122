class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        s = bin(x ^ y)
        output = 0

        for i in range(len(s)):
            if s[i] == '1':
                output += 1
        return output

# how to use bin(), oct(), hex() etc