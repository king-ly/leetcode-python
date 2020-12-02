from com.leetcode.linkedUtils import ListNode, ListNodeUtils


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lDummyHead = ListNode(-1)
        rDummyHead = ListNode(-1)
        lCur = lDummyHead
        rCur = rDummyHead
        while head:
            val = head.val
            node = ListNode(val)
            if val < x:
                lCur.next = node
                lCur = lCur.next
            else:
                rCur.next = node
                rCur = rCur.next
            head = head.next
        lCur.next = rDummyHead.next
        return lDummyHead.next


if __name__ == '__main__':
    nums = [1, 4, 3, 2, 5, 2]
    x = 3
    head = ListNodeUtils.addNodes(nums)
    res = Solution().partition(head, x)
    ListNodeUtils.printListNode(res)
