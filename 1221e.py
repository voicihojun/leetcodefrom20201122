class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countL = 0
        countR = 0
        output = 0
        for i in s:
            if i == 'R':
                countR += 1
            elif i == 'L':
                countL += 1

            if countL == countR:
                output += 1
        return output