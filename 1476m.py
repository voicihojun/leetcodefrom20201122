class SubrectangleQueries:

    def __init__(self, rectangle):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2 + 1):
            if(i <= row2):
                # for j in range(col1, col2 + 1):
                #     self.rectangle[i][j] = newValue
                self.rectangle[i][col1:col2+1] = [newValue] * len(self.rectangle[row1][col1:col2+1])
                print(self.rectangle)
                # when using the current code compare to # code,
                # memory usage is augmented slightly, but runtime is faster.
                # current code : memory usage 16.1 MB, runtime 156 ms
                # commented code : memory usage 15.9 MB, runtime 212 ms

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]

# ["SubrectangleQueries","updateSubrectangle","updateSubrectangle","getValue","getValue","getValue","updateSubrectangle"]
# [[[[5,2,5,9,4],[10,7,1,4,1],[7,3,1,3,8],[9,7,9,4,9]]],[1,0,3,3,10],[3,2,3,2,4],[2,0],[2,2],[3,4],[1,4,1,4,10]]

# s = SubrectangleQueries([[5,2,5,9,4],[10,7,1,4,1],[7,3,1,3,8],[9,7,9,4,9]])
# s.updateSubrectangle(1,0,3,3,10)
# s.updateSubrectangle(3,2,3,2,4)
# print(s.getValue(2,0))
# print(s.getValue(2,2))
# print(s.getValue(3,4))
# s.updateSubrectangle(1,4,1,4,10)



# ["SubrectangleQueries","updateSubrectangle","getValue","getValue","getValue","updateSubrectangle","getValue","updateSubrectangle","getValue","updateSubrectangle"]
# [[[[6,9,6,1,2],[8,8,6,5,9],[7,6,10,8,2],[7,7,4,9,1]]],[1,4,2,4,5],[3,4],[2,4],[3,4],[3,4,3,4,8],[2,0],[1,3,3,4,3],[0,2],[3,1,3,4,5]]

s = SubrectangleQueries([[6,9,6,1,2],[8,8,6,5,9],[7,6,10,8,2],[7,7,4,9,1]])
s.updateSubrectangle(1,4,2,4,5)
print(s.getValue(3,4))
print(s.getValue(2,4))
print(s.getValue(3,4))
s.updateSubrectangle(3,4,3,4,8)
print(s.getValue(2,0))
s.updateSubrectangle(1,3,3,4,3)
print(s.getValue(0,2))
s.updateSubrectangle(3,1,3,4,5)