from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        k = 2                           # 1-定义待交换位置
        for i in range(2, len(nums)):   #2-从待交换位置起，循环遍历数组
                                        #3-确定交换条件，当前位置与K进行交换
            if nums[i] != nums[k - 2]:  # 这里要记得，不是i-2而是k-2
                nums[k] = nums[i]
                k += 1                  #4-等交换位置k++
        return k


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    size = Solution().removeDuplicates(nums)
    print(size)
