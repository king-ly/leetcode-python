from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        双指针循环
        """
        i = 0
        k = len(nums)
        # 交换位置后，i索引不能+1，因为不知道交换后的元素的内容
        while i < k:
            if nums[i] == val:
                nums[i], nums[k - 1] = nums[k - 1], nums[i]
                k -= 1
            else:
                i += 1
        return k


if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    size = Solution().removeElement(nums, val=3)
    print(size)
