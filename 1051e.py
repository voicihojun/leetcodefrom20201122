class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        target = copy.deepcopy(heights)
        target.sort()
        print(target)
        output = 0
        if len(heights) == 0:
            return output

        for i in range(len(heights)):

            if heights[i] != target[i]:
                output += 1

        return output