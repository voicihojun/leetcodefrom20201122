class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dic = {
            "line1": "qwertyuiop",
            "line2": "asdfghjkl",
            "line3": "zxcvbnm"
        }
        result = []
        for i in words:
            output = ""
            if i[0].lower() in dic["line1"]:
                for j in i:
                    if j.lower() not in dic["line1"]:
                        output = ""
                        break
                    output += j

            elif i[0].lower() in dic["line2"]:
                for j in i:
                    if j.lower() not in dic["line2"]:
                        output = ""
                        break
                    output += j

            else:
                for j in i:
                    if j.lower() not in dic["line3"]:
                        output = ""
                        break
                    output += j

            if output != "":
                result.append(output)

        return result



