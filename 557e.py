class Solution:
    def reverseWords(self, s: str) -> str:
        l1 = s.split(" ")
        print(l1)
        for i in range(len(l1)):
            l1[i] = l1[i][::-1]

        return " ".join(l1)

# how to reverse string / how to use 'join'