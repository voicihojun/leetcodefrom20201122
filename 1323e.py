class Solution:
    def maximum69Number(self, num: int) -> int:
        output = list(str(num))

        for i in range(len(output)):
            if output[i] == '6':
                output[i] = '9'
                return int("".join(output))

        return int("".join(output))

# convert int to array and then brute force.