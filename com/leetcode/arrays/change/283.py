from typing import List

"""
移动零
思路：和最后第一个不为0的元素进行位置交换
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        找到不为0的索引，和i位置交换，时间复杂度要好
        """
        k = 0                       # 1-定义待交换位置的索引
        for i in range(len(nums)):  # 2-循环遍历数组
            if nums[i] != 0:        # 3-找到交换条件，进行交换
                nums[k], nums[i] = nums[i], nums[k]
                k += 1              # 4-交换完成后，k值++


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12, 0]
    Solution().moveZeroes(nums)
    print('移动后:{}'.format(nums))
