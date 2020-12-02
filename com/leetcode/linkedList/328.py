from com.leetcode.linkedUtils import ListNode, ListNodeUtils


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        lDummyHead = ListNode(-1)
        rDummyHead = ListNode(-1)
        lCur = lDummyHead
        rCur = rDummyHead
        i = 1
        while head:
            node = ListNode(head.val)
            if i % 2 == 1:
                lCur.next = node
                lCur = lCur.next
            else:
                rCur.next = node
                rCur = rCur.next
            head = head.next
            i += 1
        lCur.next = rDummyHead.next
        return lDummyHead.next


if __name__ == '__main__':
    nums = [2, 1, 3, 5, 6, 4, 7]
    head = ListNodeUtils.addNodes(nums)
    res = Solution().oddEvenList(head)
    ListNodeUtils.printListNode(res)
