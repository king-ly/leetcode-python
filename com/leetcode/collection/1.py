from typing import List

"""
使用字典查找表

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [dict[target - nums[i]], i]
            else:
                dict[nums[i]] = i
        return None


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    res = Solution().twoSum(nums, target)
    print(res)
