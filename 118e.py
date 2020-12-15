class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        for i in range(numRows):
            ele = []
            for j in range(i+1):
                if j == 0 or j == i:
                    ele.append(1)
                else:
                    ele.append(output[i-1][j-1] + output[i-1][j])
            output.append(ele)
        return output