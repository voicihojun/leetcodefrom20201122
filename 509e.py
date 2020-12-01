class Solution:
    def fib(self, N: int) -> int:
        fibo = [0, 1]
        for i in range(2, N + 1):
            fibo.append(fibo[i - 1] + fibo[i - 2])
        return fibo[N]

        # if N==0:
        #     return 0
        # elif N==1:
        #     return 1
        # else:
        #     a = 0
        #     b = 1
        #     for i in range(1,N):
        #         c = a + b
        #         a = b
        #         b = c
        #     return c 