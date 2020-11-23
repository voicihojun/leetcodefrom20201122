class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_num = 0
        output = []
        for i in candies:
            if max_num < i:
                max_num = i
        for j in candies:
            if j + extraCandies >= max_num:
                output.append(True)
            else:
                output.append(False)

        return output

s = Solution()

candies = [2,3,5,1,3]
extraCandies = 3  # Output: [true,true,true,false,true]

print(s.kidsWithCandies(candies, extraCandies))

"""using first for loop, search what is the greatest number in list of candies,
and then, if the sum of 'each element of list of candies' and 'extra candies' is equal or greater than the greatest number, 
return True for the element, or return False. """