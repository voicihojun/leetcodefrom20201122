class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # x = 0
        # y = 0
        output = 0
        for i in range(len(points) - 1):
            x = abs(points[i + 1][0] - points[i][0])
            y = abs(points[i + 1][1] - points[i][1])

            minimum, maximum = min(x, y), max(x, y)

            output += minimum
            output += maximum - minimum

        return output
