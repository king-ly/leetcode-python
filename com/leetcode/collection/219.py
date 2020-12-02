from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        set1 = set()
        i = 0 - k
        j = 0
        while j < len(nums):
            if nums[j] in set1:
                return True
            else:
                set1.add(nums[j])
                if i >= 0:
                    set1.remove(nums[i])
            i += 1
            j += 1
        return False


if __name__ == '__main__':
    nums = [1, 0, 1, 1]
    k = 1
    res = Solution().containsNearbyDuplicate(nums, k)
    print(res)
