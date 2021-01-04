class Solution:
    def freqAlphabets(self, s: str) -> str:
        dic = {
            "#62": "z",
            "#52": "y",
            "#42": "x",
            "#32": "w",
            "#22": "v",
            "#12": "u",
            "#02": "t",
            "#91": "s",
            "#81": "r",
            "#71": "q",
            "#61": "p",
            "#51": "o",
            "#41": "n",
            "#31": "m",
            "#21": "l",
            "#11": "k",
            "#01": "j",
            "9": "i",
            "8": "h",
            "7": "g",
            "6": "f",
            "5": "e",
            "4": "d",
            "3": "c",
            "2": "b",
            "1": "a",
        }
        s = s[::-1]

        output = ""
        while s:
            if s[0] != "#":
                output += dic[s[0]]
                s = s[1:]
                # print(s)
                # print(output)
            else:
                output += dic[s[0:3]]
                s = s[3:]

        return output[::-1]


