from com.leetcode.linkedUtils import ListNode, ListNodeUtils


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(-1)
        cur = dummyHead
        x = 0
        while l1 or l2:
            sumTmp = None
            if l1 and l2:
                sumTmp = l1.val + l2.val + x
                l1, l2 = l1.next, l2.next
            elif l1 is None:
                sumTmp = l2.val + x
                l2 = l2.next
            else:
                sumTmp = l1.val + x
                l1 = l1.next

            if sumTmp >= 10:
                x = 1
                sumTmp = sumTmp % 10
            else:
                x = 0
            node = ListNode(sumTmp)
            cur.next = node
            cur = cur.next
        if x == 1:
            node = ListNode(1)
            cur.next = node
        return dummyHead.next


if __name__ == '__main__':
    nums1 = [5]
    nums2 = [5]
    l1 = ListNodeUtils.addNodes(nums1)
    l2 = ListNodeUtils.addNodes(nums2)
    res = Solution().addTwoNumbers(l1, l2)
    ListNodeUtils.printListNode(res)
