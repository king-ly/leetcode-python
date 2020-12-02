from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_list = list(s)
        p_list = list(p)
        p_list.sort()

        l = 0
        r = l + len(p) - 1  # [l,r]
        res = []
        while r < len(s):
            tmp = s_list[l:r + 1]
            tmp.sort()
            if tmp == p_list:
                res.append(l)
            l += 1
            r += 1

        return res


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    res = Solution().findAnagrams(s, p)
    print(res)
