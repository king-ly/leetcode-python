from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1
        return i


if __name__ == '__main__':
    nums = [1, 1, 2]
    size = Solution().removeDuplicates(nums)
    print(size)
