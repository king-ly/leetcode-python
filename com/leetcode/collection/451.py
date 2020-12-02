import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        dict = collections.Counter(s)
        # sort以后变成[('e', 4), ('a', 3), ('r', 2), ('d', 1)]
        listCnt = sorted(dict.items(), key=lambda d: d[1], reverse=True)
        # print(listCnt)
        list2 = [[list[0]] * list[1] for list in listCnt]  # 二维list
        list1 = sum(list2, [])  # 一维list
        return "".join(list1)


if __name__ == '__main__':
    s = "raaeaedere"
    res = Solution().frequencySort(s)
    print(res)
