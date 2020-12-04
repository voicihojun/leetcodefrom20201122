class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.originalColor = image[sr][sc]
        output = [[sr, sc]]
        visited = [[sr, sc]]

        def helper(image, sr, sc):
            if sr + 1 < len(image) and [sr + 1, sc] not in visited:
                if self.originalColor == image[sr + 1][sc]:
                    output.append([sr + 1, sc])
                    visited.append([sr + 1, sc])
                    helper(image, sr + 1, sc)
            if sc + 1 < len(image[0]) and [sr, sc + 1] not in visited:
                if self.originalColor == image[sr][sc + 1]:
                    output.append([sr, sc + 1])
                    visited.append([sr, sc + 1])
                    helper(image, sr, sc + 1)
            if sr - 1 >= 0 and [sr - 1, sc] not in visited:
                if self.originalColor == image[sr - 1][sc]:
                    output.append([sr - 1, sc])
                    visited.append([sr - 1, sc])
                    helper(image, sr - 1, sc)
            if sc - 1 >= 0 and [sr, sc - 1] not in visited:
                if self.originalColor == image[sr][sc - 1]:
                    output.append([sr, sc - 1])
                    visited.append([sr, sc - 1])
                    helper(image, sr, sc - 1)

        helper(image, sr, sc)
        # print(output)
        for i in output:
            image[i[0]][i[1]] = newColor
        return image

