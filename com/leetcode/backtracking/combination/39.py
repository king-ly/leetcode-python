from typing import List


class Solution:
    res = list()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res.clear()
        candidates.sort()    #不排序不能剪枝
        self._helper(candidates, target, 0, list())
        return self.res

    #使用start索引进行剪枝
    def _helper(self, candidates: List[int], target: int, start: int, p: List[int]):
        s = sum(p)
        if target == s:
            x = p.copy()
            x.sort()
            if x not in self.res:           #去重
                self.res.append(x)
            return
        if s > target:
            return
        for i in range(start, len(candidates)):
            p.append(candidates[i])
            self._helper(candidates, target, start, p)
            p.pop()


if __name__ == '__main__':
    candidates = [1, 2]
    target = 4
    res = Solution().combinationSum(candidates, target)
    print(res)
