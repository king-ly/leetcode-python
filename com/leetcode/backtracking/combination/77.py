from typing import List


class Solution:
    res = list()

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res.clear()
        self._helper(n, k, 1, list())
        return self.res

    # index 代表索引位置
    def _helper(self, n: int, k: int, start: int, p: List[int]) -> None:
        if k == len(p):
            self.res.append(p.copy())
            return
        for i in range(start, n + 1):
            p.append(i)
            self._helper(n, k, i + 1, p)
            p.pop()


if __name__ == '__main__':
    n, k = 4, 2
    res = Solution().combine(n, k)
    print(res)
