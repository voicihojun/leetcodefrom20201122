class Solution:
    output = ""

    def sortString(self, s: str) -> str:
        dic = {}
        for i in s:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1

        while (dic):
            self.helper(dic)

        return self.output

    def helper(self, dic):
        k = list(dic.keys())

        k.sort()

        for i in k:
            self.output += i
            dic[i] -= 1
            if dic[i] == 0:
                del dic[i]

        # ============  reverse part
        k = list(dic.keys())

        k.sort(reverse=True)

        for i in k:
            self.output += i
            dic[i] -= 1
            if dic[i] == 0:
                del dic[i]