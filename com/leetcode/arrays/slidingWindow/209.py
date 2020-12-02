from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l, r = 0, -1                                #1-[l,r] 初始化时区间没有数值 1-定义l,r
        sumVals = 0
        minLen = len(nums) + 1
        while l < len(nums):                        #2-当l还能滑到，说明没到头。在循环里面控制r   2-如果l能滑，循环就没有结束
            if r + 1 < len(nums) and sumVals < s:   #3-右边是否还能滑动
                r += 1
                sumVals += nums[r]
            else:                                   #4-如果右边不能滑动，那么左边滑动
                sumVals -= nums[l]
                l += 1
            if sumVals >= s:
                minLen = min(minLen, r - l + 1)
        if minLen == len(nums) + 1:
            return 0
        else:
            return minLen


if __name__ == '__main__':
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    minLen = Solution().minSubArrayLen(s, nums)
    print(minLen)
