class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # if one cube has perimeter 4, but 2 cube has perimeter 6
        # because meeting line is needed not to calculate.

        # 전체 1의 개수 * 4에서 각 1포지션에서 겹치는 부분의 개수를 빼면됨
        output = 0
        print(len(grid[0]))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    output += 4
                    if i-1 >= 0 and grid[i-1][j] == 1:
                           output -= 1
                    if i+1 < len(grid) and grid[i+1][j] == 1:
                           output -= 1
                    if j-1 >= 0 and grid[i][j-1] == 1:
                           output -= 1
                    if j+1 < len(grid[0]) and grid[i][j+1] == 1:
                           output -= 1
        return output