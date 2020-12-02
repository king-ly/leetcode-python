from typing import List

"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？

"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
         只有三个数，可以使用三路快排的思想做
         两个游标 zero,two
         时间复杂度 O(n)
         空间复杂度O(1)
         只遍历了一遍list
        """
        zero = -1  # [0,zero]区间中的值为0
        two = len(nums)  # 【two,len(nums)-1】 区间中的值为2

        i = 0
        while i < two:  # 注意退出条件，当i到达two的时候，two后面的已经排序好了
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                two -= 1
                nums[i], nums[two] = nums[two], nums[i]
            else:
                assert nums[i] == 0, "非法数字"
                zero += 1
                nums[i], nums[zero] = nums[zero], nums[i]
                i += 1


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
    print(nums)
