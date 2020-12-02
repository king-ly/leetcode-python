from typing import List

from com.leetcode.linkedUtils import ListNode, ListNodeUtils
import queue


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = queue.PriorityQueue()
        for link in lists:
            while link:
                pq.put(link.val)
                link = link.next
        dummyHead = ListNode(-1)
        cur = dummyHead
        while not pq.empty():
            node = ListNode(pq.get())
            cur.next = node
            cur = cur.next
        return dummyHead.next


if __name__ == '__main__':
    nums1 = [1, 4, 5]
    nums2 = [1, 3, 4]
    nums3 = [2, 6]
    lists = [ListNodeUtils.addNodes(nums1), ListNodeUtils.addNodes(nums2), ListNodeUtils.addNodes(nums3)]
    res = Solution().mergeKLists(lists)
    ListNodeUtils.printListNode(res)
