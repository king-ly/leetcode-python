class Solution:
    def reverseVowels(self, s: str) -> str:
        strList = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self._checkVowels(strList[l]):
                l += 1
            while l < r and not self._checkVowels(strList[r]):
                r -= 1
            if l != r:
                strList[l], strList[r] = strList[r], strList[l]
            l += 1
            r -= 1
        return "".join(strList)   #list转str

    def _checkVowels(self, val):
        vowels = ['a', 'e', 'i', 'o', 'u']
        return val.lower() in vowels


if __name__ == '__main__':
    s = "hello"
    strList = Solution().reverseVowels(s)
    print(strList)
