class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # output = 0
        # for i in J:
        #     for j in S:
        #         if i == j:
        #             output += 1
        # return output

        # return sum([list(S).count(x) for x in list(J)])

        return sum(s in J for s in S)

"""After doing the first commented one, i realize that the code is not efficient compare to others. 
To learn more even if it's simple coding, I saw the others in the discussion.
The last one(not commented) is elegant and more efficient compare to others. 
"""