class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        difference = {k - v for k, v in zip(arr[1:], arr[:-1])}
        return len(difference) == 1

#     for example,
#     arr = [1,3,5,7]
#     arr[1:] = [1,3,5]
#     arr[:-1] = [3,5,7]

#     after using zip,
#     the result is
#     [(1,3), (3,5), (5,7)]
#     1-3=-2, 3-5=-2, 5-7=-2
#     difference = {-2}


