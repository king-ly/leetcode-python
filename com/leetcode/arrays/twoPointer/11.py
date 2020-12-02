from typing import List

"""
11. 盛最多水的容器
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1   #1-定义left，right
        maxAreas = 0
        while l < r:                #2-while循环 l<r
            area = min(height[l], height[r]) * (r - l)
            maxAreas = max(maxAreas, area)
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        return maxAreas


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    max = Solution().maxArea(height)
    print(max)
