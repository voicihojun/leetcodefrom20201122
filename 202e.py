class Solution:
    def isHappy(self, n: int) -> bool:
        happy_list = []

        while n != 1:
            output = 0
            for i in str(n):
                output += int(i) ** 2
            if output not in happy_list:
                happy_list.append(output)
            else:
                return False
            n = output
        return True