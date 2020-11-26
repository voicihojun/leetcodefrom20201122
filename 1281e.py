class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        product = 1
        for i in str(n):
            i = int(i)
            sum += i
            product *= i
        return product - sum

