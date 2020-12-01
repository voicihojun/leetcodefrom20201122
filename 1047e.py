class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = ""
        for i in range(len(S)):
            if stack == "":
                stack += S[i]
            else:
                if stack[-1] != S[i]:
                    stack += S[i]
                else:
                    stack = stack[:-1]
            # print(stack)
        return stack

