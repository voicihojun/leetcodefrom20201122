class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0
        for i in range(len(accounts)):
            output = 0
            for j in range(len(accounts[i])):
                output += accounts[i][j]
            if output > maxi:
                maxi = output

        return maxi
