class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        output = []
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[i] >= prices[j]:
                    output.append(prices[i] - prices[j])
                    break

            if len(output) != i + 1:
                output.append(prices[i])
        return output
