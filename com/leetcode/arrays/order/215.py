from typing import List

"""
快速排序
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self._quickSort(nums, 0, len(nums) - 1)
        return nums[-k]

    def _quickSort(self, nums, left, right):
        if left > right:
            return
        i, j = left, right
        base = nums[left]
        while i != j:
            while j > i and nums[j] > base:
                j -= 1
            while i < j and nums[i] <= base:
                i += 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[i] = nums[i], nums[left]

        self._quickSort(nums, left, i - 1)

        self._quickSort(nums, i + 1, right)


if __name__ == '__main__':
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    val = Solution().findKthLargest(nums, 4)
    print(val)
