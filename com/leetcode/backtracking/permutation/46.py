from typing import List

#排列问题
class Solution:
    res = list()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res.clear()
        self._helper(nums, list())
        return self.res

    def _helper(self, nums: List[int], p: List[int]) -> None:
        if len(nums) == len(p):
            self.res.append(p.copy())   #这里注意，由于是浅拷贝，所以p.pop的时候会把res中的元素也pop了。需要使用.copy()
            return
        for i in range(len(nums)):
            if nums[i] in p:
                continue
            p.append(nums[i])
            self._helper(nums, p)
            p.pop()

if __name__ == '__main__':
    nums = [1, 2, 3]
    res = Solution().permute(nums)
    print(res)
