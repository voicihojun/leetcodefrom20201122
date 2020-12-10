import random

class Solution:
    def sumZero(self, n: int) -> List[int]:
        output = []
        l1 = [i for i in range(1, 501)]
        for i in range(n // 2):
            # num = random.choice(l1)
            # l1.remove(num)
            num = l1.pop()
            output.extend([num, -num])
        if n % 2 == 1:
            output.append(0)

        return output