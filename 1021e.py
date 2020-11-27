class Solution:
    #     def removeOuterParentheses(self, S: str) -> str:
    #         hs = {'(' : 0, ')' : 0}
    #         output = []
    #         index = 0
    #         for i in range(len(S)):
    #             if S[i] == '(':
    #                 hs['('] += 1
    #             else:
    #                 hs[')'] += 1

    #             if hs['('] == hs[')']:
    #                 output.append(S[index+1:i])
    #                 index = i + 1

    #         return ''.join(output)
    def removeOuterParentheses(self, S: str) -> str:
        stack, res, word = [], [], ''

        for c in S:
            if c == '(':
                stack.append(c)
            else:
                stack.pop()
            word += c

            if not stack:
                if word:
                    res.append(word[1:-1])
                word = ""

        return ''.join(res)