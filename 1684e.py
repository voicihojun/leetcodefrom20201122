class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        output = len(words)
        for i in words:
            s = set(list(i))
            for j in s:
                if not j in allowed:
                    output -= 1
                    break
        return output