class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        output = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    output += len(grid[i]) - j
                    break
        return output

# binary search or brute force
