from com.leetcode.linkedUtils import ListNode, ListNodeUtils

"""
双指针 pre,cur
"""


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummyHead = ListNode(-1)
        dummyHead.next = head
        pre, cur = dummyHead, head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return dummyHead.next


if __name__ == '__main__':
    nums = [1, 2, 6, 3, 4, 5, 6]
    head = ListNodeUtils.addNodes(nums)
    val = 6
    res = Solution().removeElements(head, val)
    ListNodeUtils.printListNode(res)
