from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1 = set()
        for num in nums:
            set1.add(num)
        return len(set1) != len(nums)


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1 = set()
        for val in nums:
            if val in set1:
                return True
            else:
                set1.add(val)
        return False


if __name__ == '__main__':
    nums = [1,2,3,4]
    res = Solution2().containsDuplicate(nums)
    print(res)
