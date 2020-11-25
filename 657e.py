class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # x, y = 0, 0
        # for i in moves:
        #     if i == 'U':
        #         y += 1
        #     elif i == 'D':
        #         y -= 1
        #     elif i == 'L':
        #         x -= 1
        #     elif i == 'R':
        #         x += 1
        #     else:
        #         print("wrong input")
        # return (True if x == 0 and y == 0 else False)

        dict = {"U": 0, "D": 0, "L": 0, "R": 0}
        for letter in moves:
            dict[letter] += 1

        return (True if dict["U"] == dict["D"] and dict["L"] == dict["R"] else False)

"""The second one is better for the performance. """