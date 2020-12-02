from typing import List

"""
使用set
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        for val in nums2:
            if val in nums1:
                res.add(val)
        return res


class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # res = set(nums1).intersection(set(nums2))
        res = set(nums1) & set(nums2)
        return res


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    res = Solution2().intersection(nums1, nums2)
    print(list(res))
