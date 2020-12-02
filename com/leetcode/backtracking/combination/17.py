from typing import List

#组合问题
class Solution:
    letterMap = [
        "",
        "",
        "abc",
        "def",
        "ghi",
        "jkl",
        "mno",
        "pqrs",
        "tuv",
        "wxyz"
    ]
    res = list()

    def letterCombinations(self, digits: str) -> List[str]:
        self.res.clear()
        if digits:
            self._helper(digits, 0, "")
        return self.res

    def _helper(self, digits: str, index: int, s: str) -> None:
        if len(digits) == index:
            self.res.append(s)
            return
        x = int(digits[index])
        letters = self.letterMap[x]
        for i in range(len(letters)):
            self._helper(digits, index + 1, s + letters[i])


if __name__ == '__main__':
    digits = "23"
    res = Solution().letterCombinations(digits)
    print(res)
