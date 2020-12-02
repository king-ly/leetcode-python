class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict = {}
        sList = s.split()
        if len(pattern) != len(sList):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dict:
                """
                     防止以下情况
                    "abba" 
                    "dog dog dog dog"
                """
                if sList[i] in dict.values():
                    return False
                dict[pattern[i]] = sList[i]
            else:
                if dict[pattern[i]] != sList[i]:
                    return False
        return True


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    res = Solution().wordPattern(pattern, s)
    print(res)
