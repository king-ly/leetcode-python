class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict = {}
        newStr = str()
        for i in range(len(s)):
            if s[i] not in dict:
                # dict的values不能出现重复
                if t[i] in dict.values():
                    return False
                dict[s[i]] = t[i]
            newStr += dict[s[i]]
        return newStr == t


if __name__ == '__main__':
    s = "paper"
    t = "title"
    res = Solution().isIsomorphic(s, t)
    print(res)
