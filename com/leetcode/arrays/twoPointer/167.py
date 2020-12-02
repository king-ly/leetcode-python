from typing import List

"""
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

"""


class Solution:
    # 使用字典辅助
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        findNums = {}  # 字典，map
        for i in range(len(numbers)):
            if target - numbers[i] in findNums:
                return [findNums[target - numbers[i]], i + 1]
            findNums[numbers[i]] = i + 1
        return None


class Solution2:
    # 二分查找法,前提是有序数组
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            y = self._binarySearch(numbers, i + 1, len(numbers) - 1, target - numbers[i])
            if y is not None:
                return [i + 1, y + 1]
        return None

    def _binarySearch(self, numbers, left, right, target):
        if left > right:
            return
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] > target:
            return self._binarySearch(numbers, left, mid - 1, target)
        else:
            return self._binarySearch(numbers, mid + 1, right, target)


class Solution3:
    # 对撞指针法  时间复杂度O(n),空间复杂度O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] > target:  # 如果大于target,说明右边取值太大了
                r -= 1
            else:
                l += 1
        return None


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    vals = Solution3().twoSum(numbers, target)
    print(vals)
