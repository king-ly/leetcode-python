from typing import List
import collections
import copy


# 三元组
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for k in range(len(nums)):
            i = k + 1
            j = len(nums) - 1
            while i < j:
                if nums[k] + nums[i] + nums[j] < 0:
                    i += 1
                elif nums[k] + nums[i] + nums[j] > 0:
                    j -= 1
                else:
                    if [nums[k], nums[i], nums[j]] not in res:
                        res.append([nums[k], nums[i], nums[j]])
                    i += 1
        return res


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dict = collections.defaultdict(list)
        res = []
        for k in range(0, len(nums)):
            if 0 - nums[k] not in dict:
                for i in range(k):
                    dict[nums[i] + nums[k]].append([nums[i], nums[k]])
            else:
                dict2 = copy.deepcopy(dict[0 - nums[k]])
                for list1 in dict2:
                    list1.append(nums[k])
                    if list1 not in res:
                        res.append(list1)
        return res


if __name__ == '__main__':
    nums = [3, 0, -2, -1, 1, 2]
    res = Solution2().threeSum(nums)
    print(res)

    # s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    # d = collections.defaultdict(list)
    # for k, v in s:
    #     d[k].append(v)
    # a = sorted(d.items())
    # print(a)
