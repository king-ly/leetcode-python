from typing import List

from sortedcontainers import SortedSet


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        set1 = SortedSet()
        i = 0 - k
        j = 0
        while j < len(nums):
            if set1 and abs(nums[j] - set1[0]) <= t:
                return True
            else:
                if i >= 0 and set1:
                    set1.pop(0)
                set1.add(nums[j])
            i += 1
            j += 1
        return False


if __name__ == '__main__':
    nums = [0]
    k = 0
    t = 0
    res = Solution().containsNearbyAlmostDuplicate(nums, k, t)
    print(res)
