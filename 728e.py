class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []
        for i in range(left, right+1):
            bool = True
            for j in str(i):
                if int(j) == 0:
                    bool = False
                    break
                if i % int(j) != 0:
                    bool = False
            if bool:
                output.append(i)
        return output