class Solution:
    #     def singleNumber(self, nums: List[int]) -> int:
    #         dic = {}
    #         for i in nums:
    #             if i in dic.keys():
    #                 dic[i] += 1
    #             else:
    #                 dic[i] = 1

    #         return [k for k, v in dic.items() if v == 1][0]
    # ========================================================
    # the above one works well

    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1

        def f1(x):
            return dic[x]

        # return min(dic.keys(), key = f1)
        return min(dic.keys(), key=(lambda k: dic[k]))
        # min(l:list, 함수)
        # 바로 위 코드 의미 : dic에서 key들을 다 가져와서 각 key를 f1 함수에 넣은 값들 중
        #     최소값을 가지는 것을 선별하는 것.
        # 즉 모든 value 값들 중 최소인 것의 키를 반환