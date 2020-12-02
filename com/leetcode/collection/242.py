import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = collections.Counter(s)
        dict2 = collections.Counter(t)
        print(dict1)
        print(dict2)
        return dict1 == dict2


if __name__ == '__main__':
    s = "nagaram"
    t = "nagaram"
    res = Solution().isAnagram(s, t)
    print(res)
