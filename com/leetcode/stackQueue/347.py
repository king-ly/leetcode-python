from typing import List
import queue
import collections


# dict排序
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = collections.Counter(nums)
        sortMap = sorted(countMap.items(), key=lambda d: d[1], reverse=True)
        return [num[0] for num in sortMap[:k]]


# most_common()方法
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list1 = collections.Counter(nums).most_common(k)
        return [num[0] for num in list1]


# 使用优先队列法
class Solution3:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = list()
        pq = queue.PriorityQueue()
        cntMap = collections.Counter(nums)
        for item in cntMap.items():
            pq.put([-item[1], item[0]])
        for _ in range(k):
            res.append(pq.get()[1])
        return res


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 2, 2, 3]
    k = 2
    res = Solution3().topKFrequent(nums, k)
    print(res)
