import collections
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = list()
        dict = {}
        for nums in nums1:
            if nums in dict:  # 这里与 collections.dict不同
                dict[nums] += 1
            else:
                dict[nums] = 1

        for nums in nums2:
            if nums in dict:  # 这里与 collections.dict不同
                res.append(nums)
                dict[nums] -= 1
                if dict[nums] == 0:
                    dict.pop(nums)
        return res


class Solution2:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = list()
        dict = collections.defaultdict(int)  # 这里使用collections模块的dict
        for nums in nums1:
            dict[nums] += 1

        for nums in nums2:
            print(dict[nums])   #collection.dict如果key不存在，有默认值
            if dict[nums] > 0:
                res.append(nums)
                dict[nums] -= 1
        return res


class Solution3:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = collections.Counter(nums1)
        dict2 = collections.Counter(nums2)
        # set(nums1) & set(nums2)  取集合交集
        xdict = {i: min(dict1[i], dict2[i]) for i in set(nums1) & set(nums2)}
        list = [[key] * value for key, value in xdict.items()]  # 得到二维数组
        res = sum(list, [])  # 二维数组转一维
        return res


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2, 3]
    # res = Solution2().intersect(nums1, nums2)
    # print(res)
    dict= collections.defaultdict(int)
    print(dict)
    print(dict[3])
    print(dict)
