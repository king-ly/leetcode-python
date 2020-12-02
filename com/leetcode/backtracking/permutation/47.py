from typing import List


class Solution:
    res = list()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res.clear()
        self._help(nums, list())
        return self.res

    # p中存放index索引位置，而不是值
    def _help(self, nums: List[int], p: List[int]) -> None:
        if len(nums) == len(p):
            x = [nums[i] for i in p]
            if x not in self.res:
                self.res.append(x)
            return
        for i in range(len(nums)):
            if i in p:
                continue
            p.append(i)
            self._help(nums, p)
            p.pop()


if __name__ == '__main__':
    nums = [1, 1, 2]
    res = Solution().permuteUnique(nums)
    print(res)
