class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        output = 0

        for i in range(n):
            if i == 0:
                output = start + 2 * i
            else:
                output = output ^ (start + 2 * i)
            # print(output)
        return output