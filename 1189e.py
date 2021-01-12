class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic = {}

        for key in text:
            if key in 'balon':
                if key not in dic.keys():
                    dic[key] = 1
                else:
                    dic[key] += 1
        print(dic)

        balloon = 'balon'

        for key in dic.keys():
            balloon = balloon.replace(key, "")

        if balloon is not "":
            return 0

        ban = min([dic['b'], dic['a'], dic['n']])
        lo = min([dic['l'], dic['o']])

        if lo >= (2 * ban):
            return ban
        else:
            if lo % 2 == 0:
                return lo // 2
            else:
                return (lo - 1) // 2