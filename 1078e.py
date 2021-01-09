class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        output = []

        for i, j, k in zip(words, words[1:], words[2:]):
            if i == first and j == second:
                output.append(k)

        return output