class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        #         output = []
        #         for i in range(1, num // 2):
        #             if num % i == 0:
        #                 if i == 1:
        #                     output.append(i)
        #                 else:
        #                     output.append(i)
        #                     output.append(int(num // i))

        #         output = sum(list(set(output)))

        #         return output == num

        # The above code is time limit exceeded.

        if num <= 1:
            return False
        output = 1
        for i in range(2, math.ceil(math.sqrt(num))):
            if num % i == 0:
                output += i
                output += num // i
        return output == num