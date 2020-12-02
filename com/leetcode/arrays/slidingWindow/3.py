class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, -1                                          #1-定义一个滑动窗口
        res = 0
        lookup = set()  # 初始化一个空集合
        while l < len(s):                                     #2-left游标做为循环结束条件
            if r + 1 < len(s) and s[r + 1] not in lookup:     #3-试着向右滑动窗口 r + 1 < len(s)
                r += 1
                lookup.add(s[r])
            else:                                             #4-试着向左滑动窗口
                lookup.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
        return res


if __name__ == '__main__':
    s = "abcabcbb"
    res = Solution().lengthOfLongestSubstring(s)
    print(res)
