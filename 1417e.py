class Solution:
    def reformat(self, s: str) -> str:
        digit = "0123456789"
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        digit_l = []
        alphabet_l = []
        output = ""

        for i in s:
            if i in digit:
                digit_l.append(i)
            else:
                alphabet_l.append(i)
        if abs(len(digit_l) - len(alphabet_l)) > 1:
            return output
        else:
            if len(digit_l) > len(alphabet_l):
                for i in range(len(alphabet_l)):
                    output += digit_l[i] + alphabet_l[i]
                return output + digit_l[-1]
            elif len(digit_l) < len(alphabet_l):
                for i in range(len(digit_l)):
                    output += alphabet_l[i] + digit_l[i]
                return output + alphabet_l[-1]
            else:
                for i in range(len(digit_l)):
                    output += alphabet_l[i] + digit_l[i]
                return output


