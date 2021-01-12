class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        if int(len(candyType) / 2) < len(set(candyType)):
            return int(len(candyType) / 2)
        else:
            return len(set(candyType))